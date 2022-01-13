# Use words.txt as the file name
fname = input("Enter file name: ")


try:
    fh = open(fname)
except:
    print('File Cannot Be Opened: ', fname)
    exit()
fr = fh.read()
fu = fr.upper()
fw = fu.rstrip()

print(fw)
