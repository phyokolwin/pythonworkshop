def factorial_iterative(n) :
    result = 1
    for i in range (n) :
        result *= i + 1
    return result


factorial_iterative(5)

def factorial_recursive(n) :
    if n == 1 :
        return 1
    else :
        return n * factorial_iterative( n - 1)


factorial_recursive(5)

