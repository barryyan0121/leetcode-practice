#
# @lc app=leetcode.cn id=800 lang=python3
#
# [800] 相似 RGB 颜色
#


# @lc code=start
class Solution:
    def similarRGB(self, color):
        result = ["#"]
        for start in (1, 3, 5):
            value = int(color[start : start + 2], 16)
            digit = min(15, (value + 8) // 17)
            result.append(f"{digit:x}{digit:x}")
        return "".join(result)


# @lc code=end


if __name__ == "__main__":
    assert Solution().similarRGB("#09f166") == "#11ee66"
    assert Solution().similarRGB("#4e4e4e") == "#555555"
