def fibonacci_iterative(n):
    previous = 0
    current = 1
    for i in range(n - 1):
        current_old = current
        current = previous + current
        previous = current_old
    return current

# from fibonacci import fibonacci_iterative
fibonacci_iterative(3)
fibonacci_iterative(10)
