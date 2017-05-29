def splitSeqs(aminoseq):
    seqs = aminoseq.split('*')
    return seqs

aminoseq = 'SIRFQNCF*LYC*AAFH*VGQEG**RQRKWQKGLGGWGQ'

print(splitSeqs(aminoseq))