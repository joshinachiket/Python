import collections
#function returns top K repeated elements in num
def frequentElements(nums, k):
    return zip(*collections.Counter(nums).most_common(k))[0]


#function to fing frequency of a number in nums
def frequencyOfNum(array, num):
    counter = collections.Counter(array)
    print counter
    print (counter.values())
    print (counter.keys())
    print (counter.most_common(1))


nums = [1,1,1,2,2,3];
print frequentElements(nums, 2)
frequencyOfNum(nums, 5)
