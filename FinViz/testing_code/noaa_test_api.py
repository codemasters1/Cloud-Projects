import requests

my_headers = {'token': 'EvNbMUPqeYbdwcgyAilCIluuKUNlLghl'}
response = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets?statiodid=COOP=010957', headers=my_headers)
print(response.json())




# response = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets', headers=my_headers)
