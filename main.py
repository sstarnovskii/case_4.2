# Case-study #4
# Developers:   Drachev Nikita (),
#               Starnovskiy Sergey (),
#               Zhuravlev Alexander ()

with open('input.txt','r') as infile:
    initialtext=infile.read()
    initialtext.split(' ')

while initialtext.find('\n')!=-1:
    initialtext.replace('\n',' ')
print(initialtext)
