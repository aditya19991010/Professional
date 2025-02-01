

def main():
    # fileobj = open( filename, mode )
    # mode is a string indicating the file’s type and what you want to do with it
    # The first letter of mode indicates the operation:
        # • r means read.
        # • w means write. If the file doesn’t exist, it’s created. If the file does exist, it’s overwritten.
        # • x means write, but only if the file does not already exist.
        # • a means append (write after the end) if the file exists.
    # The second letter of mode is the file’s type:
        # • t (or nothing) means text.
        # • b means binary.

    text = '''
    Python is a good general-purpose, high-level language.
    Its design makes it very readable.
    It enables writing highly productive programs.
    '''

    print(text)
    print(len(text))

    ###  write to a file
    # The write() function returns the number of bytes written. It does not add any spaces
    # or newlines, as print() does
    fout = open('python.txt', 'wt')
    bytes_written = fout.write(text)
    print(bytes_written)
    fout.close()

    # write to a file using print
    # By default, print() adds a space after each argument and a newline at the end
    fout = open('python.txt', 'wt')
    print(text, file=fout)
    fout.close()

    # write in chunks
    fout = open('python.txt', 'wt')
    size = len(text)
    offset = 0
    chunk = 100
    while True:
        if offset > size:
            break
        bytes_written = fout.write(text[offset:offset + chunk])
        print(bytes_written)
        offset += chunk
    fout.close()

    # mode x to prevent overwriting
    try:
        fout = open('python.txt', 'xt')
        fout.write("Python libraries")
    except FileExistsError:
        print("python.txt already exists! ")
        # return None
    finally:
        print("x mode prevented overwriting!")


    ### Read a Text File with read(), readline(), or readlines()
    fin = open('python.txt', 'rt')
    ftext = fin.read()  # reads entire file in memory! caution: 1GB file occupies 1GB space in memory
    fin.close()
    print(len(ftext))

    # read in chunks
    ftext = ''
    fin = open('python.txt', 'rt')
    chunk = 100
    while True:
        fragment = fin.read(chunk)  # returns empty string ('') after read till the end
        if not fragment:
            break
        ftext += fragment
    fin.close()
    print(len(ftext))

    # read a line at a time
    ftext = ''
    fin = open('python.txt', 'rt')
    while True:
        line = fin.readline()
        if not line:
            break
        ftext += line
    fin.close()
    print(len(ftext))

    # read a text file using an iterator - the preferred way
    ftext = ''
    fin = open('python.txt', 'rt')
    for line in fin:
        ftext += line
    fin.close()
    print(len(ftext))

    # readlines()
    fin = open('python.txt', 'rt')
    lines = fin.readlines()
    fin.close()
    print(len(lines), 'lines read')
    for line in lines:
        print(line, end='')

    ### Binary files
    # Write a Binary File with write()
    # If you include a 'b' in the mode string, the file is opened in binary mode. In this case,
    # you read and write bytes instead of a string.
    bdata = bytes(range(0, 256))
    print(len(bdata))
    fout = open('bfile.bin', 'wb')
    bytes_written = fout.write(bdata)
    print(bytes_written)
    fout.close()

    # one can write binary data also in chunks similar to strings

    # Read a Binary File with read()
    fin = open('bfile.bin', 'rb')
    bdata = fin.read()
    print(len(bdata))
    fin.close()

    # Close Files Automatically by Using with
    # The file should be closed to force any remaining writes to be completed
    # Python has context managers to clean up things such as open files. You use the form with expression as variable.
    # After the block of code under the context manager (in this case, one line)
    # completes (normally or by a raised exception), the file is closed automatically.
    with open('python.txt', 'wt') as fout:
        fout.write(text)

    # Change Position with seek()
    # As you read and write, Python keeps track of where you are in the file. The tell()
    # function returns your current offset from the beginning of the file, in bytes. The
    # seek() function lets you jump to another byte offset in the file. This means that you
    # don’t have to read every byte in a file to read the last one; you can seek() to the last
    # one and just read one byte.
    fin = open('bfile.bin', 'rb')
    print(fin.tell())
    print(fin.seek(255))
    bdata = fin.read()
    print(len(bdata))
    print(bdata[0])
    # You can call seek() with a second argument: seek( offset, origin ):
        # • If origin is 0 (the default), go offset bytes from the start
        # • If origin is 1, go offset bytes from the current position
        # • If origin is 2, go offset bytes relative to the end
    # These values are also defined in the standard os module:
    import os
    print(os.SEEK_SET)
    print(os.SEEK_CUR)
    print(os.SEEK_END)
    # read last byte in different ways
    fin = open('bfile.bin', 'rb')
    print(fin.seek(-1, 2)) # One byte before the end of the file
    print(fin.tell())

    fin = open('bfile.bin', 'rb')
    print(fin.seek(254, 0))
    print(fin.seek(1, 1))

    ### Structured text files
    # There are many formats, and here’s how you can distinguish them:
    # • A separator, or delimiter, character like tab ('\t'), comma (','), or vertical bar
    # ('|'). This is an example of the comma-separated values (CSV) format.
    # • '<' and '>' around tags. Examples include XML and HTML.
    # • Punctuation. An example is JavaScript Object Notation (JSON).
    # • Indentation. An example is YAML (which depending on the source you use
    # means “YAML Ain’t Markup Language;” you’ll need to research that one your‐
    # self).
    # • Miscellaneous, such as configuration files for programs.
    import csv
    # write to a csv file from a list of lists
    players = [
        ['Rohit', 'Sharma'],
        ['Shubham', 'Gill'],
        ['Virat', 'Kohli'],
        ['Rahul', 'K L'],
        ['Hardik', 'Pandya']
    ]
    with open("players.txt", 'wt') as fout:
        csvout = csv.writer(fout)
        csvout.writerows(players)

    # read from a csv file
    with open("players.txt", 'rt') as fin:
        cin = csv.reader(fin)
        p = [row for row in cin]
        print(p)

    # read into a dict using DictReader()
    with open("players.txt", 'rt') as fin:
        cin = csv.DictReader(fin, fieldnames=['first', 'last'])
        p = [row for row in cin]
        print(p)

    # write using DictWriter()
    p1 = [
        {'first': 'Jasprit', 'last': 'Bumrah'},
        {'first': 'Mohammed', 'last': 'Siraj'},
        {'first': 'Hardik', 'last': 'Pandya'},
        {'first': 'Kuldeep', 'last': 'Yadav'},
        {'first': 'Ravindra', 'last': 'Jadeja'},
    ]
    with open('players1.txt', 'wt') as fout:
        cout = csv.DictWriter(fout, ['first', 'last'])
        cout.writeheader()
        cout.writerows(p1)
    # read back in
    with open("players1.txt", 'rt') as fin:
        cin = csv.DictReader(fin)
        p = [row for row in cin]
        print(p)

    ### XML files
    import xml.etree.ElementTree as et
    tree = et.ElementTree(file='menu.xml')
    root = tree.getroot()
    print(root.tag)
    for child in root:
        print('tag:', child.tag, 'attributes:', child.attrib)
        for grandchild in child:
            print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

    # other python libraries for XML processing
    # xml.dom
    # xml.sax

    ### HTML files

    ### JSON files
    import json
    menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }
    # encode the dict data structure (menu) to a JSON string (menu_json) by using dumps()
    menu_json = json.dumps(menu)
    print(menu_json)
    # let’s turn the JSON string menu_json back into a Python data structure (menu2) by using loads()
    menu2 = json.loads(menu_json)
    print(menu2)


    ### serialize by using pickle
    # Saving data structures to a file is called serializing.
    # Python provides the pickle module to save and restore any object in a special binary format.
    import pickle
    import datetime
    now1 = datetime.datetime.utcnow()
    print(now1)
    pickled = pickle.dumps(now1)
    now2 = pickle.loads(pickled)
    print(now2)

    ### other file formats
    # spreadsheets - xlrd
    # HDF5 - h5py, PyTables








if __name__ == "__main__":
   main()