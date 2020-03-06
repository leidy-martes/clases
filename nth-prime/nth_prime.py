def prime(number):
    if number == 0:
        raise ValueError("there is no 0th prime integer")
    if number == 1:
        return 2
    primes = []
    candidate = 2
    while len(primes) != number:
        is_prime = True
        for j in range(0, len(primes)):
            if candidate % primes[j] == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
        if candidate % 2 == 0:
            candidate += 1
    return primes[-1]
