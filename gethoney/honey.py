import os

directory = os.listdir(path=".")


def txt_finder(dir):
    for file in dir:
        if file[-4:] == ".txt":
            f = open(file, "r")
            print(f.read())
            f.close()
