"""2708. 一个群组的最大强度"""


class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        maximum = minimum = nums[0]
        for value in nums[1:]:
            candidates = (maximum, minimum, value, maximum * value, minimum * value)
            maximum, minimum = max(candidates), min(candidates)
        return maximum


if __name__ == "__main__":
    assert Solution().maxStrength([-9, -3, 0, 2, 4]) == 216
