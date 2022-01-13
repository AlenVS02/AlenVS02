#7.2 Write a program that prompts for a file name, then opens that file and reads through the
# file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the
# average of those values and produce an output as shown below. Do not use the sum() function or
# a variable named sum in your solution.

avr = 0
x = 0

fnam = input('Enter File Name:')

try:
    fnnam = open(fnam)
except:
    print('File Not Found. Please, try again.')
    exit()

for line in fnnam:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        avr = avr + 1
        strx = line.strip('X-DSPAM-Confidence:')
        strxf = float(strx)
        x = x + strxf
print('Average spam confidence:', x/avr)
