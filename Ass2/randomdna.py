length = input('Length: ')

lengthInt = int(length)

import random

sequence = ''

for i in range(lengthInt):
    nuc = random.choice('AGCT')
    sequence += nuc

print('>myrandomsequence')
print(sequence)
