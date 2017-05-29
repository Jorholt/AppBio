def splitFile(file):
    data = ''
    outdata = []
    for line in file:
        data += line

    splitData = data.split('>')
    for element in splitData:
        newElement = '>' + element
        outdata.append(newElement)
    return outdata

def readSequence(data):
    header = ''
    sequence = ''
    splitData = data.split('\n')
    for line in splitData:
        if line.startswith('>'):
            header = line.rstrip()
        else:
            seq = line.rstrip()
            sequence += seq
    return header, sequence

def reverseDNA(sequence):
    reverse = ''

    for nuc in sequence:
        if nuc == 'A':
            reverse += 'T'
        elif nuc == 'T':
            reverse += 'A'
        elif nuc == 'G':
            reverse += 'C'
        elif nuc == 'C':
            reverse += 'G'

    return reverse[::-1]

aminoacids = {'TTT' : 'F', 'TTC' : 'F', 'TTA' : 'L', 'TTG' : 'L', 'CTT' : 'L', 'CTC' : 'L', 'CTA' : 'L', 'CTG' : 'L',
              'ATT' : 'I', 'ATC' : 'I', 'ATA' : 'I', 'ATG' : 'M', 'GTT' : 'V', 'GTC' : 'V', 'GTA' : 'V', 'GTG' : 'V',
              'TCT' : 'S', 'TCC' : 'S', 'TCA' : 'S', 'TCG' : 'S', 'CCT' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
              'ACT' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T', 'GCT' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
              'TAT' : 'Y', 'TAC' : 'Y', 'CAT' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'AAT' : 'N', 'AAC' : 'N',
              'AAA' : 'K', 'AAG' : 'K', 'GAT' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E', 'TGT' : 'C', 'TGC' : 'C',
              'TGG' : 'W', 'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGT' : 'S', 'AGC' : 'S', 'AGA' : 'R',
              'AGG' : 'R', 'GGT' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G', 'TAA' : '*', 'TAG' : '*', 'TGA' : '*'
              }

def translateDNA(sequence, start = 0):
    aminoseq = ''
    for i in range(start, len(sequence)-2, 3):
        codon = sequence[i:i+3]
        if codon in aminoacids:
            aminoseq += aminoacids[codon]
        else:
            aminoseq += 'X'
    return aminoseq

def splitSeqs(aminoseq):
    seqs = aminoseq.split('*')
    return seqs

def stopDistance(aminoseqs):
    longest = ''
    for seq in aminoseqs:
        if len(seq) > len(longest):
            longest = seq
    return longest

entry = input('Which file? ')
file = open(entry)

seqList = splitFile(file)

for i in range(1, len(seqList)):
    header, sequence = readSequence(seqList[i])
    print(header)
    SEQUENCE = sequence.upper()
    reverseSEQ = reverseDNA(SEQUENCE)
    forward1 = translateDNA(SEQUENCE, start=0)
    forward2 = translateDNA(SEQUENCE, start=1)
    forward3 = translateDNA(SEQUENCE, start=2)
    reverse1 = translateDNA(reverseSEQ, start=0)
    reverse2 = translateDNA(reverseSEQ, start=1)
    reverse3 = translateDNA(reverseSEQ, start=2)
    F1_split = splitSeqs(forward1)
    F2_split = splitSeqs(forward2)
    F3_split = splitSeqs(forward3)
    R1_split = splitSeqs(reverse1)
    R2_split = splitSeqs(reverse2)
    R3_split = splitSeqs(reverse3)
    combinedSeqs = F1_split + F2_split + F3_split + R1_split + R2_split + R3_split
    longestORF = stopDistance(combinedSeqs)
    print(longestORF)
    print(len(longestORF))