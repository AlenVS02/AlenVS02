webster = dict()
sender = list()

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print("File Name Invalid. Please Try Again.")
    exit()

for line in fh:
    if not line.startswith('From '):
         continue
    else:
         str2 = line.split(' ')
         sender.append(str2[1])
for word in sender:
    webster[word] = webster.get(word,0) + 1

name = None
reps = 0

for key,value in webster.items():
    if name == value or value > reps:
        name = key
        reps = value

print(name,reps)
