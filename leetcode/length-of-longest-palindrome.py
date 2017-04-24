
import collections
def longestPalindromeSize(string):
#first let us find all the letters that appear odd number if times
    odds = sum (count & 1 for count in collections.Counter(string).values())
    return len(string) - odds + bool(odds)

print longestPalindromeSize("abccccdd")
