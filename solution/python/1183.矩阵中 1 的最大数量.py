#
# @lc app=leetcode.cn id=1183 lang=python3
#
# [1183] 矩阵中 1 的最大数量
#


# @lc code=start
class Solution:
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        counts = []
        for row in range(sideLength):
            for column in range(sideLength):
                counts.append(
                    ((width - row - 1) // sideLength + 1)
                    * ((height - column - 1) // sideLength + 1)
                )
        return sum(sorted(counts, reverse=True)[:maxOnes])


# @lc code=end


if __name__ == "__main__":
    test_cases = [((3, 3, 2, 1), 4), ((3, 3, 2, 2), 6)]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().maximumNumberOfOnes(*args) == expected, index
