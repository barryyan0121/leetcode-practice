from typing import List


class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        size = 1 << n
        merged = [[] for _ in range(size)]
        length = [0] * size
        median = [0] * size
        for mask in range(1, size):
            bit = mask & -mask
            i = bit.bit_length() - 1
            rest = mask ^ bit
            a, b = lists[i], merged[rest]
            result = []
            x = y = 0
            while x < len(a) and y < len(b):
                if a[x] <= b[y]:
                    result.append(a[x])
                    x += 1
                else:
                    result.append(b[y])
                    y += 1
            result.extend(a[x:])
            result.extend(b[y:])
            merged[mask] = result
            length[mask] = len(result)
            median[mask] = result[(len(result) - 1) // 2]

        dp = [0] * size
        for mask in range(1, size):
            if mask & (mask - 1) == 0:
                continue
            best = 10**30
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if sub < other:
                    best = min(
                        best,
                        dp[sub]
                        + dp[other]
                        + length[mask]
                        + abs(median[sub] - median[other]),
                    )
                sub = (sub - 1) & mask
            dp[mask] = best
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.minMergeCost([[1, 3, 5], [2, 4], [6, 7, 8]]) == 18
    assert s.minMergeCost([[1, 1, 5], [1, 4, 7, 8]]) == 10
    assert s.minMergeCost([[1], [3]]) == 4
    assert s.minMergeCost([[1], [1]]) == 2
