from typing import List


class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        mod = 10**9 + 7
        n = len(perm)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod

        bit = [0] * (n + 1)

        def add(i: int, delta: int) -> None:
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & -i

        def query(i: int) -> int:
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        ans = 0
        for i, x in enumerate(perm):
            smaller = x - 1 - query(x - 1)
            ans = (ans + smaller * fact[n - 1 - i]) % mod
            add(x - 1, 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.getPermutationIndex([1, 2, 3]) == 0
    assert s.getPermutationIndex([1, 3, 2]) == 1
    assert s.getPermutationIndex([2, 1, 3]) == 2
    print("3109 ok")
