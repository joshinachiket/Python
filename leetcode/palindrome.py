def isPalindrome(string):
    flag = False
    if(str(string) == str(string)[::-1]):
        flag = True
    return flag

print isPalindrome("1221")
