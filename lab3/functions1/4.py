def filter_prime(n):
    new = []
    t = True
    for num in n:
        if num > 1:
            for i in range(2, (num//2)+1):
                if (num % i) == 0:
                    t = False #print(num, "is not a prime number")
                    break
            else:
                t = True #print(num, "is a prime number")
        else:
            t = False #print(num, "is not a prime number")
        if t == True:
            new.append(num)
    
    return new
    



a = list(map(int, input().split()))
print(* filter_prime(a))