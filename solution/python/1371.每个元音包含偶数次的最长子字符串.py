# @lc app=leetcode.cn id=1371 lang=python3


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = {0: -1}
        mask = result = 0
        bits = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        for index, char in enumerate(s):
            mask ^= bits.get(char, 0)
            if mask in first:
                result = max(result, index - first[mask])
            else:
                first[mask] = index
        return result


if __name__ == "__main__":
    test_cases = [
        (Solution().findTheLongestSubstring, ("eleetminicoworoep",), 13),
        (Solution().findTheLongestSubstring, ("leetcodeisgreat",), 5),
        (Solution().findTheLongestSubstring, ("bcbcbc",), 6),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1371 题 "每个元音包含偶数次的最长子字符串" 所有测试用例通过')
