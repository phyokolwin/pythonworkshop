 # Find the Least Common Multiple of Two Divisors
counting = True
first_divisor = 24
second_divisor = 36
i = 1
while counting:
    if i % first_divisor == 0 and i % second_divisor == 0:
        print('The Least Common Multiple of', first_divisor, 'and', second_divisor, 'is', i, '.')
        break
    i += 1
