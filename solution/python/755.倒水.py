#
# @lc app=leetcode.cn id=755 lang=python3
#
# [755] 倒水
#


# @lc code=start
class Solution:
    def pourWater(self, heights, volume: int, k: int):
        for _ in range(volume):
            position = k
            for candidate in range(k - 1, -1, -1):
                if heights[candidate] > heights[candidate + 1]:
                    break
                if heights[candidate] < heights[position]:
                    position = candidate
            if position != k:
                heights[position] += 1
                continue
            position = k
            for candidate in range(k + 1, len(heights)):
                if heights[candidate] > heights[candidate - 1]:
                    break
                if heights[candidate] < heights[position]:
                    position = candidate
            if position != k:
                heights[position] += 1
            else:
                heights[k] += 1
        return heights


# @lc code=end


if __name__ == "__main__":
    assert Solution().pourWater([2, 1, 1, 2, 1, 2, 2], 4, 2) == [2, 2, 3, 2, 2, 2, 2]
