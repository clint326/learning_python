def fact(n):
    if n < 1:
        return 'Can\'t calculate factorial of a number less than 1'
    elif n == 1:
        return 1
    else:
        return (n * fact(n-1))
