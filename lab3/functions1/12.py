def histogrsm(a):
    for i in a:
        print(i*"*")


a = list(map(int, input().split()))
histogrsm(a)