import os

#Include the Lambda layer extracted location
os.environ['AWS_DATA_PATH'] = '/opt/' 

import boto3
import time
import datetime
import json

region = os.environ['AWS_REGION']

try:
    data_set_id = os.environ['DATA_SET_ID']
except KeyError:
    raise Exception("DATA_SET_ID environment variable must be defined!") 

try:
    product_id = os.environ['PRODUCT_ID']
except KeyError:
    raise Exception("PRODUCT_ID environment variable must be defined!")

def lambda_handler(event, context):
    # Setup the boto3 clients needed
    dataexchange = boto3.client(
        service_name='dataexchange',
        region_name=region

    )
    marketplace_catalog = boto3.client(
        service_name='marketplace-catalog',
        region_name=region
    )

    # parse the s3 details from the triggered event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    print('bucket_name:', bucket_name)
    print('object_key:', object_key)

    # CREATE REVISION under the dataset provided as an environment variable
    current_time_for_creating_revision = datetime.datetime.utcnow().strftime("%d %B %Y %I:%M%p UTC")
    create_revision_response = dataexchange.create_revision(DataSetId=data_set_id, Comment='Revision created programmatically on ' + current_time_for_creating_revision)
    revision_id = create_revision_response['Id']

    print('revision_id:', revision_id) #it prints it here

    # CREATE JOB under the revision to import file from S3 to DataExchange
    create_job_s3_import = dataexchange.create_job(
        Type='IMPORT_ASSETS_FROM_S3',
        Details={
            'ImportAssetsFromS3': {
                'DataSetId': data_set_id,
                'RevisionId': revision_id,
                'AssetSources': [
                    {
                        'Bucket': bucket_name,
                        'Key': object_key
                    }

                ]
            }
        }
    )

    # Filter the ID of the Job from the response
    job_id = create_job_s3_import['Id']
    print(job_id)

    # invoke START JOB on the created job to change it from Waiting to Completed state
    start_created_job = dataexchange.start_job(JobId=job_id)

    # GET JOB details to track the state of the job and wait until it reaches COMPLETED state
    job_status = ''

    while job_status != 'COMPLETED':
        get_job_status = dataexchange.get_job(JobId=job_id)
        print(job_id)
        job_status = get_job_status['State']
        print('Job Status ' + job_status)
        
        if job_status=='ERROR' :
            job_errors = get_job_status['Errors']
            print('Job_errors=', job_errors)
            raise Exception('JobId: {} failed with error:{}'.format(job_id, job_errors))
        
        time.sleep(.5)
        
    # Finalize revision by invoking UPDATE REVISION
    current_time_for_finalize_revision = datetime.datetime.utcnow().strftime("%d %B %Y %I:%M%p UTC")
    print(current_time_for_finalize_revision)
    finalize_revision = dataexchange.update_revision(DataSetId=data_set_id, RevisionId=revision_id, Finalized=True, Comment='Revision finalized programmatically on ' + current_time_for_finalize_revision)

    # New dataset version created and finalized, now let’s add it to an existing product specified as an env variable

    # Describe Product details to get the metadata about the product
    describe_entity = marketplace_catalog.describe_entity(Catalog='AWSMarketplace', EntityId=product_id)

    # Use the output to pull out producttype, productid and datasetarn for startchangeset call
    entity_type = describe_entity['EntityType']
    entity_id = describe_entity['EntityIdentifier']
    dataset_arn = ((json.loads(describe_entity['Details']))['DataSets'][0]['DataSetArn'])
    revision_arn = create_revision_response['Arn']
 
# cce3e903e8ff7a664d46e5cc38dbdd3a
# prod-jv6njdco4pclu

    # StartChangeSet to add the newly finalized revision to an existing product
    start_change_set = marketplace_catalog.start_change_set(
        Catalog='AWSMarketplace',
        ChangeSetName="Adding revision to my Product",
        ChangeSet=[
            {
                "ChangeType": "AddRevisions",
                "Entity": {
                    "Identifier": entity_id,
                    "Type": entity_type
                },
                "Details": json.dumps({
                    "DataSetArn": dataset_arn,
                    "RevisionArns": [revision_arn]
                })
            }
        ]
    )
    
    #Filter the changeset id from the response
    changeset_id = start_change_set['ChangeSetId']

    # DESCRIBE CHANGESET to get the status of the changeset and wait until it reaches SUCCEEDED state
    change_set_status = ''

    while change_set_status != 'SUCCEEDED':
        describe_change_set = marketplace_catalog.describe_change_set(
            Catalog='AWSMarketplace',
            ChangeSetId=changeset_id
            )
        change_set_status = describe_change_set['Status']
        print('Change Set Status ' + change_set_status)

        if change_set_status=='FAILED' :
            print(describe_change_set)
            failurereason = describe_change_set['FailureDescription']
            raise Exception('ChangeSetID: {} failed with error:\n{}'.format(changeset_id, failurereason))
        time.sleep(1)
        
    return ('Your data has been published successfully')