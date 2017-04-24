def twoSum(num, target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i + 1
        else:
            return map[num[i], i + 1]
    return -1 -1

num = [2, 3, 4, 5, 1]
map = twoSum(num, 9)

print map
