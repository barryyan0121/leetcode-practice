#
# @lc app=leetcode.cn id=1180 lang=python3
#
# [1180] 统计只含单一字母的子串
#


# @lc code=start
class Solution:
    def countLetters(self, s):
        result = length = 0
        previous = ""
        for character in s + "#":
            if character == previous:
                length += 1
            else:
                result += length * (length + 1) // 2
                previous, length = character, 1
        return result


# @lc code=end


if __name__ == "__main__":
    test_cases = [(("aaaba",), 8), (("aaaaaaaaaa",), 55)]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().countLetters(*args) == expected, index
