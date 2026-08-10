"""2318. 不同骰子序列的数目"""

from math import gcd


class Solution:
    def distinctSequences(self, n: int) -> int:
        mod = 1_000_000_007
        if n == 1:
            return 6
        states = {(0, face): 1 for face in range(1, 7)}
        for _ in range(1, n):
            nxt = {}
            for (previous_previous, previous), count in states.items():
                for face in range(1, 7):
                    if (
                        face != previous
                        and face != previous_previous
                        and gcd(face, previous) == 1
                    ):
                        key = (previous, face)
                        nxt[key] = (nxt.get(key, 0) + count) % mod
            states = nxt
        return sum(states.values()) % mod
