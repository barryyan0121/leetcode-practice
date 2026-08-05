"""3854. 使数组奇偶交替的最少操作"""


class Solution:
    def makeParityAlternating(self, nums: list[int]) -> list[int]:
        minimum_operations = min(
            sum(value % 2 != (index + start) % 2 for index, value in enumerate(nums))
            for start in (0, 1)
        )
        best_range = 10**30
        for start in (0, 1):
            wrong = [
                index
                for index, value in enumerate(nums)
                if value % 2 != (index + start) % 2
            ]
            if len(wrong) != minimum_operations:
                continue
            wrong_set = set(wrong)
            fixed = [
                value for index, value in enumerate(nums) if index not in wrong_set
            ]
            lows = {min(nums) - 1, min(nums), min(nums) + 1}
            highs = {max(nums) - 1, max(nums), max(nums) + 1}
            if fixed:
                lows.add(min(fixed))
                highs.add(max(fixed))
            for low in lows:
                for high in highs:
                    if low > high or any(
                        value < low or value > high for value in fixed
                    ):
                        continue
                    if all(
                        low <= nums[index] - 1 <= high or low <= nums[index] + 1 <= high
                        for index in wrong
                    ):
                        best_range = min(best_range, high - low)
        return [minimum_operations, best_range]


if __name__ == "__main__":
    test_cases = [
        (([-2, -3, 1, 4],), [2, 6]),
        (([0, 2, -2],), [1, 3]),
        (([7],), [0, 0]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().makeParityAlternating(*args) == expected
