from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for count in candiesCount:
            prefix.append(prefix[-1] + count)
        result = []
        for candy_type, day, cap in queries:
            before = prefix[candy_type]
            total = prefix[candy_type + 1]
            result.append(day + 1 <= total and (day + 1) * cap > before)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.canEat(
        [7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
    ) == [True, False, True]
    assert solution.canEat([5, 2, 6, 4, 1], [[3, 1, 2], [4, 10, 3]]) == [False, True]
    print("1744 passed")
