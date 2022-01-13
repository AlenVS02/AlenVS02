'''Write a program to read through the mbox-short.txt and figure out the distribution by
hour of the day for each of the messages. You can pull the hour out from the 'From ' line by
finding the time and then splitting the string a second time using a colon.
Once you have accumulated the counts for each hour, print out the counts, sorted by hour
as shown below.'''


webster = dict()
hours = list()

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
         str3 = str2[6].split(':')
         hours.append(str3[0])
for hour in hours:
    webster[hour] = webster.get(hour,0) + 1

[print(k,v) for k,v in sorted([(k,v) for k,v in webster.items()])]
