class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        prime = [True] * (n + 1)
        prime[0:2] = [False, False]
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                prime[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
        return [[i, n - i] for i in range(2, n // 2 + 1) if prime[i] and prime[n - i]]


if __name__ == "__main__":
    assert Solution().findPrimePairs(10) == [[3, 7], [5, 5]]
