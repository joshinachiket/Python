def removeElement(nums, val):
    answer = 0;
    for num in nums:
        if num != val:
            nums[answer] = num
            answer = answer + 1
    return answer

nums = [3, 2, 2, 3, 4, 5, 6]
answer = removeElement(nums, 5)
print answer
