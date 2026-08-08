#
# @lc app=leetcode.cn id=1199 lang=python3
#
# [1199] 建造街区的最短时间
#


# @lc code=start
import heapq


class Solution:
    def minBuildTime(self, blocks, split):
        heapq.heapify(blocks)
        while len(blocks) > 1:
            first = heapq.heappop(blocks)
            second = heapq.heappop(blocks)
            heapq.heappush(blocks, max(first, second) + split)
        return blocks[0]


# @lc code=end


if __name__ == "__main__":
    test_cases = [(([1, 2], 5), 7), (([1, 2, 3], 1), 4)]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().minBuildTime(*args) == expected, index
