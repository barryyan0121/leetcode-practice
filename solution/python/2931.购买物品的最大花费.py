"""2931. 购买物品的最大花费"""


class Solution:
    def maxSpending(self, values: list[list[int]]) -> int:
        items = sorted(value for row in values for value in row)
        return sum((index + 1) * value for index, value in enumerate(items))


if __name__ == "__main__":
    assert Solution().maxSpending([[8, 5, 2], [6, 4, 1], [9, 7, 3]]) == 285
