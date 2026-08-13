"""2377. 根据第 K 个分数对学生进行排序"""


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=lambda row: row[k], reverse=True)


if __name__ == "__main__":
    assert Solution().sortTheStudents(
        [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2
    ) == [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]
