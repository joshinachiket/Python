import math
#bin (x) : Converts an integer number to a binary string. The result is a valid Python expression.
def hammingDistance(num1, num2):
    return bin(num1 ^ num2).count('1')

#finds number of bits set in anumber
def countSetBits(num):
    return bin(num).count('1')

#flip bits of  number
def reverseBits(num):
    maxNum = 0
    i = 0
    while (maxNum < num):
        maxNum = maxNum + math.pow(2, i)
        i+=1
    return maxNum - num

#find the bits of the number and return first set bit
def findBits(nums):
    num_bits = 8
    bits = [(nums >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]
    for i in range(len(bits)):
        if (bits[i] == 1):
            print i
            return
    print bits

print hammingDistance(1, 4)
print countSetBits(15)
print reverseBits(6)
findBits(19)
