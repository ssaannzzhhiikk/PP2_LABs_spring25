def is_palindrome(txt):
    new_txt = "".join(filter(str.isalnum, txt)).lower()
    return new_txt == new_txt[::-1]

print(is_palindrome('ab"bsb"b-a'))

print(is_palindrome("abaa"))