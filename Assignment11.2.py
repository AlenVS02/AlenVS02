import re
from time import perf_counter

Start_time = perf_counter()
firu = open('regex_sum_1365544.txt')
suma = 0
for line in firu:
    Word = re.findall('[0-9]+', line)
    for x in Word:
        suma = suma + int(x)
print(suma)
Stop_time = perf_counter()

print(Stop_time-Start_time)

Start_time = perf_counter()
print(sum([int(x) for x in re.findall('[0-9]+',open('regex_sum_1365544.txt').read())]))
Stop_time = perf_counter()

print(Stop_time-Start_time)