def palindrome(a):
    if a == a[::-1]:
        return True
    return False
a = input()
print(palindrome(a))


def histogrsm(a):
    for i in a:
        print(i*"*")


b = list(map(int, input().split()))
histogrsm(b)