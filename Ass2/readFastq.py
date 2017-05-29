entry = input('Enter fastq(.fq) filename: ')
file = open(entry)

numseq = 0
seqlist = []

for line in file:
    if line.startswith('@'):
        seq = line[1:].rstrip()
        seqlist.append(seq)
        numseq += 1

print(numseq)
for acc in seqlist:
    print(acc)
