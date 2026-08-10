"""2974. 最小数字游戏"""


class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        return [
            value
            for index in range(0, len(nums), 2)
            for value in (nums[index + 1], nums[index])
        ]


if __name__ == "__main__":
    assert Solution().numberGame([5, 4, 2, 3]) == [3, 2, 5, 4]
