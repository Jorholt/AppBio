def stopDistance(aminoseqs):
    longest = ''
    for seq in aminoseqs:
        if len(seq) > len(longest):
            longest = seq
    return longest

listofseqs = ['ap', 'appl', 'a', 'apple', 'app']

print(stopDistance(listofseqs))