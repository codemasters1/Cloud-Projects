f = open("test-file.txt", "w")
f.write("Testing Fargate running task correctly running to a S3 bucket!")
f.close()

#open and read the file after the appending:
# f = open("test-file.txt", "r")
# print(f.read())