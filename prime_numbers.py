def is_prime(x):
    if type(x) is int and x >= 2:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False
    
def prime100():
    c, i = 0, 0
    while c < 100:
        if is_prime(i):
            print(i)
            c += 1
        i += 1

# generate the first 100 prime numbers
prime100()
