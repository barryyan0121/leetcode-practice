from bisect import bisect_left
from typing import List


class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        machines = sorted(zip(costs, capacity))
        prefix = []
        best = 0
        for cost, cap in machines:
            best = max(best, cap) if cost < budget else best
            prefix.append(best)
        for i, (cost, cap) in enumerate(machines):
            limit = budget - cost
            j = bisect_left(machines, (limit, -10**30), 0, i)
            if j:
                best = max(best, cap + prefix[j - 1])
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxCapacity([4, 8, 5, 3], [1, 5, 2, 7], 8) == 8
    assert s.maxCapacity([3, 5, 7, 4], [2, 4, 3, 6], 7) == 6
    assert s.maxCapacity([2, 2, 2], [3, 5, 4], 5) == 9
