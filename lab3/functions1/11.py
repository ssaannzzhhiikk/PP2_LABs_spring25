def palindrome(a):
    if a == a[::-1]:
        return True
    return False


a = input()

print(palindrome(a))