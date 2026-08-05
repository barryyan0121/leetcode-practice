"""3587. 最小相邻交换至奇偶交替"""


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        even_positions = [index for index, value in enumerate(nums) if value % 2 == 0]
        n = len(nums)
        if abs(len(even_positions) - (n - len(even_positions))) > 1:
            return -1
        costs = []
        for start in (0, 1):
            targets = list(range(start, n, 2))
            if len(targets) == len(even_positions):
                costs.append(sum(abs(a - b) for a, b in zip(even_positions, targets)))
        return min(costs) if costs else -1


if __name__ == "__main__":
    test_cases = [
        (([2, 4, 6, 5, 7],), 3),
        (([2, 4, 5, 7],), 1),
        (([1, 2, 3],), 0),
        (([4, 5, 6, 8],), -1),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minSwaps(nums) == expected
