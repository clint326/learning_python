def fact(n):
    """
    This is a simple factorial program to demonstrate recursive programming.
    """
    if n < 0:
        return 'Can\'t calculate factorial of a number less than 0'
    elif n == 0 or n == 1:
        return 1
    else:
        return (n * fact(n-1))

# demonstrate with 100!
print(fact(100))
