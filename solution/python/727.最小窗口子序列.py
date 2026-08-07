#
# @lc app=leetcode.cn id=727 lang=python3
#
# [727] 最小窗口子序列
#


# @lc code=start
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        best = ""
        starts = [-1] * len(s2)
        for end, char in enumerate(s1):
            for j in range(len(s2) - 1, -1, -1):
                if char == s2[j]:
                    starts[j] = end if j == 0 else starts[j - 1]
            if starts[-1] >= 0:
                window = s1[starts[-1] : end + 1]
                if not best or len(window) < len(best):
                    best = window
        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.minWindow("abcdebdde", "bde") == "bcde"
