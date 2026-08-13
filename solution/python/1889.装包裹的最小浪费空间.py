from bisect import bisect_right
from typing import List


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        mod = 10**9 + 7
        packages.sort()
        prefix = [0]
        for value in packages:
            prefix.append(prefix[-1] + value)
        answer = float("inf")
        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < packages[-1]:
                continue
            previous = 0
            wasted = 0
            for box in supplier:
                end = bisect_right(packages, box, previous)
                wasted += box * (end - previous) - (prefix[end] - prefix[previous])
                previous = end
                if previous == len(packages):
                    break
            answer = min(answer, wasted)
        return -1 if answer == float("inf") else answer % mod

if __name__ == "__main__":
    solver = Solution()
    assert solver.minWastedSpace([2, 3, 5], [[4, 8], [2, 8]]) == 6
    assert solver.minWastedSpace([2, 3, 5], [[1, 4], [2, 3]]) == -1
