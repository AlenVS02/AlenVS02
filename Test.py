x = input('Enter File Name:')
try:
    y = open(x)
except:
    open('mbox.txt',r)

for line in y:
    print(line)
