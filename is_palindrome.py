def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False

def is_p_spaces(string):
    #string = "".join([x.strip() for x in string])
    string = [x for x in string if x == ' ']
    return is_palindrome(string)

print is_palindrome("abcde")
print is_palindrome("abcba")
print is_palindrome("abccba")
print is_p_spaces("abc cba")
print is_p_spaces("ab cb a")
