"""3232. 判断数字游戏能否获胜"""


class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        return sum(num if num < 10 else -num for num in nums) != 0


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 10], False),
        ([1, 2, 3, 4, 5, 14], True),
        ([5, 5, 5, 25], True),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().canAliceWin(nums) == expected
