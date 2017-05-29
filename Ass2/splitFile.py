entry = input('Which file? ')
file = open(entry)

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

output = splitFile(file)
print(output)