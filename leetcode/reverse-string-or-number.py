def reverseString(string):
    if len(string) <= 1:
        return string

    return reverseString(string[1:]) + string[0];

temp = reverseString("1234");
print(temp);
