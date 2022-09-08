f = open("test-file.txt", "w")
f.write("Testing version 2, CLI to s3")
f.close()

f = open("test-file.txt", "r")
print(f.read())