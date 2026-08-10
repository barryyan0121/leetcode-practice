"""2478. 完美分割的方案数"""


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        mod = 10**9 + 7
        prime = set("2357")
        previous = [0] * (len(s) + 1)
        previous[0] = 1
        for _ in range(k):
            current = [0] * (len(s) + 1)
            ways = 0
            for end in range(1, len(s) + 1):
                start = end - minLength
                if start >= 0 and s[start] in prime:
                    ways = (ways + previous[start]) % mod
                if s[end - 1] not in prime:
                    current[end] = ways
            previous = current
        return previous[len(s)]
