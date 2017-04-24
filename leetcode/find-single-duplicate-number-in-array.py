def findSingleNumber(num):
    answer = 0;
    for i in num:
        answer = answer ^ i
    return answer

num = [2,3,1,1,3]
print findSingleNumber(num)
