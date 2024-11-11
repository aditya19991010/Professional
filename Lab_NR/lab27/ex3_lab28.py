with open('../../../../.config/JetBrains/PyCharmCE2024.2/scratches/example.txt', mode='w') as file:
    file.write('''Hello, this is written from Python\n,This is the second line''')

with open('../../../../.config/JetBrains/PyCharmCE2024.2/scratches/example.txt', mode='r') as file:
    for row in file:
        print(row)



##modify this
with open('../../../../.config/JetBrains/PyCharmCE2024.2/scratches/example.txt', mode='r+') as file:
    print(file.readlines(2))
    mod_lines = ''' This is the modified 2nd line '''
    file.writelines(mod_lines)
    print(file.readlines())
