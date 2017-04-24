def checkIfPower2(num):
    return (num !=0) and (num & (num - 1)) == 0

print checkIfPower2(7)
