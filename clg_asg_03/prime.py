
def print_primes():
    for i in range(2, 101):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):  # Loop till the square root of i
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

print_primes()

