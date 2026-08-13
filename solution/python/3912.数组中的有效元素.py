"""3912. 数组中的有效元素"""


class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        right_max = [0] * len(nums)
        right_max[-1] = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            right_max[index] = max(nums[index], right_max[index + 1])
        answer = []
        left_max = float("-inf")
        for index, value in enumerate(nums):
            if value > left_max or (
                value > right_max[index + 1] if index + 1 < len(nums) else True
            ):
                answer.append(value)
            left_max = max(left_max, value)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 4, 2, 3, 2],), [1, 2, 4, 3, 2]),
        (([5, 4, 3],), [5, 4, 3]),
        (([2, 2, 2],), [2, 2]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findValidElements(*args) == expected
