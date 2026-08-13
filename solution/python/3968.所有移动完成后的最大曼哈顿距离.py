#
# @lc app=leetcode.cn id=3968 lang=python3
#
# [3968] 所有移动完成后的最大曼哈顿距离
#


class Solution:
    # @lc code=start
    def maxDistance(self, moves: str) -> int:
        horizontal = moves.count("R") - moves.count("L")
        vertical = moves.count("U") - moves.count("D")
        wildcards = moves.count("_")
        return abs(horizontal) + abs(vertical) + wildcards

    # @lc code=end


if __name__ == "__main__":
    test_cases = [
        (("L_D_",), 4),
        (("U_R",), 3),
        (("__",), 2),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxDistance(*args) == expected
