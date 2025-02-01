#Files
import os
print(os.getcwd())
text  = ''' 
Hey, There is a fruit seller near HMT nagar.
The vendor is creating a big mess in the market with his astonishing sales strategies.
'''

fout = open('../../../.config/JetBrains/PyCharmCE2024.2/scratches/python.txt', 'wt')
bytes_written = fout.write(text)

print(bytes_written)
fout.close()

# write in chunks
fout = open('../../../.config/JetBrains/PyCharmCE2024.2/scratches/python.txt', 'wt')
size = len(text)
offset = 0
chunk = 100
while True:
    if offset > chunk:
        break
    bytes_written = fout.write(text[offset:offset + chunk])
    print(bytes_written)
    offset += chunk
fout.close()