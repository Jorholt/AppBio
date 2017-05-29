entry = input('Which file? ')
file = open(entry)

def readSequence(file):
    header = ''
    sequence = ''
    for line in file:
        if line.startswith('>'):
            header = line.rstrip()
        else:
            seq = line.rstrip()
            sequence += seq
    return header, sequence

header, sequence = readSequence(file)
print(header)
print(sequence)