#
# @lc app=leetcode.cn id=1182 lang=python3
#
# [1182] 与目标颜色间的最短距离
#

from bisect import bisect_left


# @lc code=start
class Solution:
    def shortestDistanceColor(self, colors, queries):
        positions = {color: [] for color in range(1, 4)}
        for index, color in enumerate(colors):
            positions[color].append(index)
        result = []
        for index, color in queries:
            matches = positions[color]
            if not matches:
                result.append(-1)
                continue
            insertion = bisect_left(matches, index)
            distances = []
            if insertion:
                distances.append(index - matches[insertion - 1])
            if insertion < len(matches):
                distances.append(matches[insertion] - index)
            result.append(min(distances))
        return result


# @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]]), [3, 0, 3]),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().shortestDistanceColor(*args) == expected, index
