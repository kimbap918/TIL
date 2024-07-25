while True:
    bitString = input()
    if bitString == '#':
        break
    p = bitString[-1]
    bitString = bitString[:-1]
    bitCnt = bitString.count('1')
    if p == 'e':
        if bitCnt % 2 == 0:
            bitString += '0'
        else:
            bitString += '1'
    else:
        if bitCnt % 2 == 0:
            bitString += '1'
        else:
            bitString += '0'
    print(bitString)