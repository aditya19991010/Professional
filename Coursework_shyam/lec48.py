try:
    fout = open("../../../.config/JetBrains/PyCharmCE2024.2/scratches/python.txt", 'xt')
    fout.write("Python libraries")
except FileExistsError:
    print("File already exist")
finally:
    print("x mode prevented overwriting!")


#read a text file with read(), readline() or readlines()
#read in chunks

ftext = ''
fin = open('../../../.config/JetBrains/PyCharmCE2024.2/scratches/python.txt', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    ftext += line
fin.close()
print(len(ftext))

# Use 'in' operator for reading lines in python

fin = open('../../../.config/JetBrains/PyCharmCE2024.2/scratches/python.txt', 'rt')
lines = fin.readlines()
print(type(lines))
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')



##Binary files
bdata = bytes(range(0,256))
print("\n",len(bdata))

text = "The vendor is creating a big mess in the market with his astonishing sales strategies."
with open("../../../.config/JetBrains/PyCharmCE2024.2/scratches/python.txt", 'wt') as fout: #closes the file itself
    fout.write(text)
    print(fout)

#tell() - Shows the position of the file, seek() - to seek the information at particular position in the file

#seek - os.SEEK_SET, os.SEEK_CUR, os.SEEK_END

#csv, XML - Extended Markup language, JSON - JavaScript object Notation

