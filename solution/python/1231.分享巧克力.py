from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        low, high = 1, sum(sweetness) // (k + 1)
        while low < high:
            target = (low + high + 1) // 2
            total = pieces = 0
            for value in sweetness:
                total += value
                if total >= target:
                    pieces += 1
                    total = 0
            if pieces >= k + 1:
                low = target
            else:
                high = target - 1
        return low


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6)]
    for _, (sweetness, k, expected) in enumerate(test_cases):
        assert Solution().maximizeSweetness(sweetness, k) == expected
