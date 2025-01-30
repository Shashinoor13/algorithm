import math
import random

# pick a number in range 1,n-1
# checl pow(a,n-1) % n !=1 return composite
# else return probably prime

def fermat_test(number,k):
    for i in range(0,k):
        a = random.randint(1,number-1)
        if pow(a,number-1,number) != 1:
            return "composite"
    return "probably prime"

def miller_rabin_test(number,k)->str:
    # assign s and d such that s >0 d>0 and d is odd
    s = 0
    d = number-1

    while d % 2 ==0:
        d = d //2
        s +=1
    
    a = random.randint(2,number-2)
    x = pow(a,d,number)
    if x == -1 or x==1:
        return "probably prime"
    else:
        y = pow(x,2,number)
        for _ in range(0,s-1):
            if y == 1 and x !=1 and x != number-1:
                return "composite"
            x = y
        if y != 1:
            return "composite"
    return "probably prime"

def main():
    number = 561
    k = 5
    print(fermat_test(number,k))
    print(miller_rabin_test(number,k))

if __name__ == "__main__":
    main()