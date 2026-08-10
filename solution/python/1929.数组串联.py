"""1929. 数组串联"""


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums


if __name__ == "__main__":
    assert Solution().getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
