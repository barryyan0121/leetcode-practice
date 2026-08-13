from typing import List


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        def cost(left, right):
            total = prefix[right] - prefix[left]
            return total * (total + 1) // 2

        inf = 10**30
        previous = [inf] * (n + 1)
        previous[0] = 0
        for groups in range(1, k + 1):
            current = [inf] * (n + 1)

            def solve(lo, hi, opt_lo, opt_hi):
                if lo > hi:
                    return
                mid = (lo + hi) // 2
                best_value, best_index = inf, opt_lo
                for j in range(opt_lo, min(opt_hi, mid - 1) + 1):
                    value = previous[j] + cost(j, mid)
                    if value < best_value:
                        best_value, best_index = value, j
                current[mid] = best_value
                solve(lo, mid - 1, opt_lo, best_index)
                solve(mid + 1, hi, best_index, opt_hi)

            solve(groups, n, groups - 1, n - 1)
            previous = current
        return previous[n]


if __name__ == "__main__":
    assert Solution().minPartitionScore([5, 1, 2, 1], 2) == 25
    assert Solution().minPartitionScore([1, 2, 3, 4], 1) == 55
    assert Solution().minPartitionScore([1, 1, 1], 3) == 3
