def count_primes(num):
    # check for 0 and 1
    if num < 2:
        return 0
    #2 or greater
    primes = [2]
    # counter going upto input num
    x = 3

    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(count_primes(100))
