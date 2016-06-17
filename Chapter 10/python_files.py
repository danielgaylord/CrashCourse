filename = 'python_files.txt'

with open(filename) as file:
    print(file.read())

print()
with open(filename) as file:
    for line in file.readlines():
        print(line.rstrip())

print()
with open(filename) as file:
    lines = file.readlines()

text = ''
for line in lines:
    text += line.strip() + " "

text = text.replace('file', 'document')
print(text)

