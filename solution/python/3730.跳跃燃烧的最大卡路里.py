"""3730. 跳跃燃烧的最大卡路里"""


class Solution:
    def maxCaloriesBurnt(self, heights: list[int]) -> int:
        heights.sort()
        order = [0] * len(heights)
        order[::2] = heights[len(heights) // 2 :][::-1]
        order[1::2] = heights[: len(heights) // 2]
        return order[0] ** 2 + sum((a - b) ** 2 for a, b in zip(order, order[1:]))


if __name__ == "__main__":
    test_cases = [([1, 7, 9], 181), ([5, 2, 4], 38), ([3, 3], 9)]
    for _, (heights, expected) in enumerate(test_cases):
        assert Solution().maxCaloriesBurnt(heights) == expected
