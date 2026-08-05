"""1835. 所有数对按位与结果的异或和"""


class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        first = 0
        for value in arr1:
            first ^= value
        second = 0
        for value in arr2:
            second ^= value
        return first & second


if __name__ == "__main__":
    test_cases = [(([1, 2, 3], [6, 5]), 0), (([12], [4]), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().getXORSum(*args) == expected
