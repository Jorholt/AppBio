#Function that splits sequences in input file into a list
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

#Splits input data (string) into header and sequence wihtout newline
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

#Takes a DNA sequence as inputs and returns the complimnetary strand
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

#Dictonary of codons -> aminoacids
aminoacids = {'TTT' : 'F', 'TTC' : 'F', 'TTA' : 'L', 'TTG' : 'L', 'CTT' : 'L', 'CTC' : 'L', 'CTA' : 'L', 'CTG' : 'L',
              'ATT' : 'I', 'ATC' : 'I', 'ATA' : 'I', 'ATG' : 'M', 'GTT' : 'V', 'GTC' : 'V', 'GTA' : 'V', 'GTG' : 'V',
              'TCT' : 'S', 'TCC' : 'S', 'TCA' : 'S', 'TCG' : 'S', 'CCT' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
              'ACT' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T', 'GCT' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
              'TAT' : 'Y', 'TAC' : 'Y', 'CAT' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'AAT' : 'N', 'AAC' : 'N',
              'AAA' : 'K', 'AAG' : 'K', 'GAT' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E', 'TGT' : 'C', 'TGC' : 'C',
              'TGG' : 'W', 'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGT' : 'S', 'AGC' : 'S', 'AGA' : 'R',
              'AGG' : 'R', 'GGT' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G', 'TAA' : '*', 'TAG' : '*', 'TGA' : '*'
              }

#Translates DNA sequence into aminoacid seqeunce
def translateDNA(sequence, start = 0):
    aminoseq = ''
    for i in range(start, len(sequence)-2, 3):
        codon = sequence[i:i+3]
        if codon in aminoacids:
            aminoseq += aminoacids[codon]
        else:
            aminoseq += 'X'
    return aminoseq

#Splits an aminoacid sequence by stopcodons(*) into a list
def splitSeqs(aminoseq):
    seqs = aminoseq.split('*')
    return seqs

#Takes a list of aminoacid sequences and returns the longest sequence
def stopDistance(aminoseqs):
    longest = ''
    for seq in aminoseqs:
        if len(seq) > len(longest):
            longest = seq
    return longest

#Asks for input file and opens said file
entry = input('Which file? ')
file = open(entry)

#Uses the function splitFile to create a list of sequences
seqList = splitFile(file)

#Iterates over sequences in seqList
for i in range(1, len(seqList)):
    #Extracts header and seqeunce from item in seqList using the function readSequence
    header, sequence = readSequence(seqList[i])
    print(header)
    #Capitalizes the sequence incase the sequence is lowercase
    SEQUENCE = sequence.upper()
    #Produces the compliment to the original sequence using the function reverseDNA
    reverseSEQ = reverseDNA(SEQUENCE)
    #Translates and saves the DNA sequence in all six reading frames using the function translateDNA
    forward1 = translateDNA(SEQUENCE, start=0)
    forward2 = translateDNA(SEQUENCE, start=1)
    forward3 = translateDNA(SEQUENCE, start=2)
    reverse1 = translateDNA(reverseSEQ, start=0)
    reverse2 = translateDNA(reverseSEQ, start=1)
    reverse3 = translateDNA(reverseSEQ, start=2)
    #Splits the sequence in all readingframes into lists of ORFs using the function splitSeqs
    F1_split = splitSeqs(forward1)
    F2_split = splitSeqs(forward2)
    F3_split = splitSeqs(forward3)
    R1_split = splitSeqs(reverse1)
    R2_split = splitSeqs(reverse2)
    R3_split = splitSeqs(reverse3)
    #Combines all six list of ORFs into one
    combinedSeqs = F1_split + F2_split + F3_split + R1_split + R2_split + R3_split
    #Gets the longest ORF from the combined list using the function stopDistance
    longestORF = stopDistance(combinedSeqs)
    print(longestORF)
    #print(len(longestORF))