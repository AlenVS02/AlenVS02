text = "X-DSPAM-Confidence:    0.8475"
numfun_1 = text.find('0')
fullint = text[numfun_1:]
float(fullint)
print(fullint)
