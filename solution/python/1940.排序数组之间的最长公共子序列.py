"""1940. 排序数组之间的最长公共子序列"""


class Solution:
    def longestCommonSubsequence(self, arrays: list[list[int]]) -> list[int]:
        common = set(arrays[0])
        for array in arrays[1:]:
            common &= set(array)
        return [value for value in arrays[0] if value in common]


if __name__ == "__main__":
    test_cases = [(([[1, 3, 4], [1, 4, 7]],), [1, 4])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().longestCommonSubsequence(*args) == expected
