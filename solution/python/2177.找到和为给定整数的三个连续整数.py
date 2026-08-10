"""2177. 找到和为给定整数的三个连续整数"""


class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3:
            return []
        middle = num // 3
        return [middle - 1, middle, middle + 1]


if __name__ == "__main__":
    assert Solution().sumOfThree(33) == [10, 11, 12]
    assert Solution().sumOfThree(4) == []
