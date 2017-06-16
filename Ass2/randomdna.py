length = input('Length: ')

lengthInt = int(length)

import random

sequence = ''

for i in range(lengthInt):
    nuc = random.choices('AGCT', [30, 20, 30, 20])
    sequence += nuc[0]

print('>myrandomsequence')
print(sequence)
