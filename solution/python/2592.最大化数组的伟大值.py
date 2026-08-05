"""2592. 最大化数组的伟大值"""


class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums.sort()
        right = 0
        for value in nums:
            if value > nums[right]:
                right += 1
        return right


if __name__ == "__main__":
    test_cases = [(([1, 3, 5, 2, 1, 3, 1],), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximizeGreatness(*args) == expected
