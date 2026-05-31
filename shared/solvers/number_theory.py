"""Programmatic math helpers extracted from AIMO3 foundation solver."""


def mod_pow(base: int, exp: int, mod: int) -> int:
    if mod == 1:
        return 0
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result


def divisors(n: int) -> list[int]:
    if n <= 0:
        return []
    out: list[int] = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            out.append(i)
            if i != n // i:
                out.append(n // i)
    return sorted(out)


def euler_totient(n: int) -> int:
    result = n
    p = 2
    t = n
    while p * p <= t:
        if t % p == 0:
            while t % p == 0:
                t //= p
            result -= result // p
        p += 1
    if t > 1:
        result -= result // t
    return result


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]


def comb(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result
