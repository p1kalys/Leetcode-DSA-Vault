from typing import List

class Solution:
    def sieve_of_eratosthenes(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        primes = []
        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)

        return primes

    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = self.sieve_of_eratosthenes(n)
        res = []
        i, j = 0, len(primes) - 1

        while i <= j:
            x, y = primes[i], primes[j]
            if x + y == n:
                res.append([x, y])
                i += 1
                j -= 1
            elif x + y < n:
                i += 1
            else:
                j -= 1

        return res
