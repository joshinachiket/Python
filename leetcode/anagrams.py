def isAnagram (word1, word2):
    word1 = sorted(word1)
    word2 = sorted(word2)
    flag = False;
    if (word1 == word2):
        flag = True;

    return flag

word1 = "gandhi"
word2 = "dhigana"

print isAnagram(word1, word2)
