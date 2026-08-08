#
# @lc app=leetcode.cn id=1181 lang=python3
#
# [1181] 前后拼接
#


# @lc code=start
class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        result = set()
        for index, first in enumerate(phrases):
            for second in phrases[index + 1 :]:
                if first.split()[-1] == second.split()[0]:
                    result.add(first + second[len(second.split()[0]) :])
                if second.split()[-1] == first.split()[0]:
                    result.add(second + first[len(first.split()[0]) :])
        return sorted(result)


# @lc code=end


if __name__ == "__main__":
    test_cases = [
        ((["writing code", "code rocks"],), ["writing code rocks"]),
        ((["a b", "b a", "a b"],), ["a b a", "b a b"]),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().beforeAndAfterPuzzles(*args) == expected, index
