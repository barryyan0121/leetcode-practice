#
# @lc app=leetcode.cn id=1153 lang=python3
#
# [1153] 字符串转化
#


# @lc code=start
class Solution:
    def canConvert(self, str1, str2):
        mapping = {}
        for source, target in zip(str1, str2):
            if source in mapping and mapping[source] != target:
                return False
            mapping[source] = target
        return str1 == str2 or len(set(str2)) < 26


# @lc code=end


if __name__ == "__main__":
    test_cases = [
        (("aabcc", "ccdee"), True),
        (("leetcode", "codeleet"), False),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().canConvert(*args) == expected, index
