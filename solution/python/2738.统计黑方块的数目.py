"""2738. 统计黑方块的数目"""


class Solution:
    def countBlackBlocks(
        self, m: int, n: int, coordinates: list[list[int]]
    ) -> list[int]:
        blocks = {}
        for row, column in coordinates:
            for top in (row - 1, row):
                for left in (column - 1, column):
                    if 0 <= top < m - 1 and 0 <= left < n - 1:
                        blocks[(top, left)] = blocks.get((top, left), 0) + 1
        answer = [0] * 5
        for count in blocks.values():
            answer[count] += 1
        answer[0] = (m - 1) * (n - 1) - sum(answer[1:])
        return answer


if __name__ == "__main__":
    assert Solution().countBlackBlocks(3, 3, [[0, 0], [1, 1], [2, 2]]) == [
        0,
        2,
        2,
        0,
        0,
    ]
