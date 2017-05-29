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

out = reverseDNA('AGTCAGTC')
print(out)