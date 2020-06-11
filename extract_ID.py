import sys

#get name. add extension, initialize filestream
name = sys.argv[1] + ".zip"
fin = open("files.txt", "r")

#read lines from file searching for matching name, extract ID & print
str = fin.readline()
while not name in str:
    str = fin.readline()
id = str.split()[0]
print(id)
