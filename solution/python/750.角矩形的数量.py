#
# @lc app=leetcode.cn id=750 lang=python3
#
# [750] 角矩形的数量
#


# @lc code=start
class Solution:
    def countCornerRectangles(self, grid) -> int:
        pairs = {}
        answer = 0
        for row in grid:
            columns = [i for i, value in enumerate(row) if value]
            for i, left in enumerate(columns):
                for right in columns[i + 1 :]:
                    key = (left, right)
                    answer += pairs.get(key, 0)
                    pairs[key] = pairs.get(key, 0) + 1
        return answer


# @lc code=end


if __name__ == "__main__":
    assert (
        Solution().countCornerRectangles(
            [
                [1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0],
            ]
        )
        == 1
    )
