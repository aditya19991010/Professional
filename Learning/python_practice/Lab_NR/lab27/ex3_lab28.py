import os
os.chdir("../../../../.config/JetBrains/PyCharmCE2024.2/scratches/")

with open('example.txt', mode='w') as file:
    file.write('''Hello, this is written from Python\n,This is the second line''')

with open('example.txt', mode='r') as file:
    for row in file:
        print(row)

##modify this
with open('example.txt', mode='r') as file:
    data = file.readlines()

data[1] = ''' This is the modified 2nd line '''

with open('example.txt', mode='w') as file:
    file.writelines(data)

with open('example.txt', mode='r') as file:
    data = file.readlines()
    print(data)
