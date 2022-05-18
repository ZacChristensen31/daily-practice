# Problem comes from CodeWars
# Solved on Wednesday May 18th, 2022

"""
    Given a number n, return the prime decomposition of n in the form (x**y)(i**j)(k**l)
"""
def solve(n: int) -> str:
    current_prime = 2
    primes = {}

    while n >= current_prime ** 2:
        if n % current_prime == 0:
            if current_prime in primes.keys():
                primes[current_prime] += 1
            else:
                primes[current_prime] = 1
            n = int(n / current_prime)

        else:
            current_prime += 1

    if n in primes.keys():
        primes[n] += 1
    else:
        primes[n] = 1

    output_string = ''.join([
        f'({k}**{v})' if v > 1
        else f'({k})'
        for k, v in primes.items()
    ])

    return output_string

if __name__ == '__main__':
    assert solve(1) == '(1)'
    assert solve(4) == '(2**2)'
    assert solve(12) == '(2**2)(3)'
    assert solve(864) == '(2**5)(3**3)'
    assert solve(86240) == '(2**5)(5)(7**2)(11)'
