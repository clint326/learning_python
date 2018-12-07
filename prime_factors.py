def is_prime(x):
    if type(x) is int and x >= 2:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False

def pf(x): # prime factors
    result=[]
    for i in range(2, x):
        if x % i == 0 and is_prime(i):
            result.append(i)
    if len(result) == 0:
        return str(x) + " is prime!"
    else:
        return result
