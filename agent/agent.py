import os


files = os.listdir(".")
print(files)

for file in files:
    open_file = open(file, "r")
    for line in open_file:
        print(line)
    open_file.close()