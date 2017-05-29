aminoacids = {'TTT' : 'F', 'TTC' : 'F', 'TTA' : 'L', 'TTG' : 'L', 'CTT' : 'L', 'CTC' : 'L', 'CTA' : 'L', 'CTG' : 'L',
              'ATT' : 'I', 'ATC' : 'I', 'ATA' : 'I', 'ATG' : 'M', 'GTT' : 'V', 'GTC' : 'V', 'GTA' : 'V', 'GTG' : 'V',
              'TCT' : 'S', 'TCC' : 'S', 'TCA' : 'S', 'TCG' : 'S', 'CCT' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
              'ACT' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T', 'GCT' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
              'TAT' : 'Y', 'TAC' : 'Y', 'CAT' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'AAT' : 'N', 'AAC' : 'N',
              'AAA' : 'K', 'AAG' : 'K', 'GAT' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E', 'TGT' : 'C', 'TGC' : 'C',
              'TGG' : 'W', 'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGT' : 'S', 'AGC' : 'S', 'AGA' : 'R',
              'AGG' : 'R', 'GGT' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G', 'TAA' : '*', 'TAG' : '*', 'TGA' : '*'
              }

def translateDNA(sequence, start = 2):
    aminoseq = ''
    for i in range(start, len(sequence)-2, 3):
        codon = sequence[i:i+3]
        print(codon)
        if codon in aminoacids:
            aminoseq += aminoacids[codon]
        else:
            aminoseq += 'X'
    return aminoseq

print(translateDNA('ATCAAA'))