import sys

name = sys.argv[1] + ".zip"
fin = open("foo.txt", "r")
str = fin.readline()
while not name in str:
    str = fin.readline()
id = str.split()[0]
print(id)
