#
# @lc app=leetcode.cn id=681 lang=python3
#
# [681] 最近时刻
#


# @lc code=start
class Solution:
    def nextClosestTime(self, time: str) -> str:
        allowed = set(time.replace(":", ""))
        current = int(time[:2]) * 60 + int(time[3:])
        for offset in range(1, 24 * 60 + 1):
            minute = (current + offset) % (24 * 60)
            candidate = f"{minute // 60:02d}:{minute % 60:02d}"
            if set(candidate.replace(":", "")) <= allowed:
                return candidate
        return time


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.nextClosestTime("19:34") == "19:39"
    assert solution.nextClosestTime("23:59") == "22:22"
