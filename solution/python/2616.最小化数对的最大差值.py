"""2616. 最小化数对的最大差值"""


class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            middle = (left + right) // 2
            pairs = index = 0
            while index + 1 < len(nums):
                if nums[index + 1] - nums[index] <= middle:
                    pairs += 1
                    index += 2
                else:
                    index += 1
            if pairs >= p:
                right = middle
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    test_cases = [(([10, 1, 2, 7, 1, 3], 2), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimizeMax(*args) == expected
