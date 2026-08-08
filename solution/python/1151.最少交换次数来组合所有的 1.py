#
# @lc app=leetcode.cn id=1151 lang=python3
#
# [1151] 最少交换次数来组合所有的 1
#


# @lc code=start
class Solution:
    def minSwaps(self, data):
        width = sum(data)
        if width <= 1:
            return 0
        zeros = best = data[:width].count(0)
        for index in range(width, len(data)):
            zeros += data[index - width] - data[index]
            best = min(best, zeros)
        return best


# @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([1, 0, 1, 0, 1],), 1),
        (([0, 0, 0, 1, 0],), 0),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().minSwaps(*args) == expected, index
