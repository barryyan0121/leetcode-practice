#
# @lc app=leetcode.cn id=660 lang=python3
#
# [660] 移除 9
#


# @lc code=start
class Solution:
    def newInteger(self, n: int) -> int:
        digits = []
        while n:
            n, digit = divmod(n, 9)
            digits.append(str(digit))
        return int("".join(reversed(digits)))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.newInteger(9) == 10
    assert solution.newInteger(10) == 11
