#
# @lc app=leetcode.cn id=1198 lang=python3
#
# [1198] 找出所有行中最小公共元素
#


# @lc code=start
class Solution:
    def smallestCommonElement(self, mat):
        common = set(mat[0])
        for row in mat[1:]:
            common &= set(row)
        return min(common, default=-1)


# @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]],), 5),
        (([[1, 2], [2, 3]],), 2),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().smallestCommonElement(*args) == expected, index
