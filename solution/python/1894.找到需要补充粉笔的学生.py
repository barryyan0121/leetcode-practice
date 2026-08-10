"""1894. 找到需要补充粉笔的学生"""


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        k %= sum(chalk)
        for index, amount in enumerate(chalk):
            if k < amount:
                return index
            k -= amount
        return 0


if __name__ == "__main__":
    assert Solution().chalkReplacer([5, 1, 5], 22) == 0
