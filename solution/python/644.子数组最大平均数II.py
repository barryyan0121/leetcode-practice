#
# @lc app=leetcode.cn id=644 lang=python3
#
# [644] 子数组最大平均数 II
#


# @lc code=start
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        low, high = min(nums), max(nums)
        while high - low > 1e-5:
            mid = (low + high) / 2
            prefix = [0]
            for value in nums:
                prefix.append(prefix[-1] + value - mid)
            minimum = 0
            possible = False
            for i in range(k, len(prefix)):
                minimum = min(minimum, prefix[i - k])
                if prefix[i] - minimum >= 0:
                    possible = True
                    break
            if possible:
                low = mid
            else:
                high = mid
        return low


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert abs(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-4
