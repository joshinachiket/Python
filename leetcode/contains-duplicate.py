import random
import collections
#function that return a random number
def get_random_ints(n_possibilities, n_samples):
    return [random.randint(1, n_possibilities) for x in xrange(n_samples)]

#function that finds if array has a duplicate
def ifDuplicate(array):
    return len(array) != len(set(array))

#function that finds the duplicate number in the array
def findDuplicate(array):
    answer = {}
    for x in array:
        if x in answer:
            answer[x] += 1
        else:
            answer[x] = 1
    print [x for x, y in answer.items() if y > 1]


print ifDuplicate(get_random_ints(10, 12))
print findDuplicate([1,2,3,2,1,5,6,5,5,5])
