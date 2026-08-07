#
# @lc app=leetcode.cn id=774 lang=python3
#
# [774] 最小化去加油站的最大距离
#


# @lc code=start
class Solution:
    def minmaxGasDist(self, stations, k):
        left, right = 0.0, stations[-1] - stations[0]
        for _ in range(60):
            middle = (left + right) / 2
            needed = sum(int((b - a) / middle) for a, b in zip(stations, stations[1:]))
            if needed > k:
                left = middle
            else:
                right = middle
        return right


# @lc code=end


if __name__ == "__main__":
    assert abs(Solution().minmaxGasDist([1, 2, 3, 4, 5], 1) - 1.0) < 1e-6
    assert abs(Solution().minmaxGasDist([1, 2, 3, 4, 5], 4) - 0.5) < 1e-6
