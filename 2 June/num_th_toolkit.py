import math

def is_prime(n:int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def sieve_of_eratosthenes(n: int) -> list[int]:
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return [i for i in range(n + 1) if is_prime[i]]


def toolkit(a : int, b: int, mod : int):
    print(f"Is Prime = {is_prime({a})}")
    print(f"GCD = gcd({a}, {b})")
    print(f"LCM = lcm({a}, {b})")
    print(f"Primes up to {a} = sieve_of_eratosthenes({a})")
    print(f"({a} * {b}) % {mod} = {(a * b) % mod}")
    print(f"({a} + {b}) % {mod} = {(a + b) % mod}")
    
toolkit(12, 18, 7)


