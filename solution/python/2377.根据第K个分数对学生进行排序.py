"""2377. 根据第 K 个分数对学生进行排序"""


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=lambda row: row[k], reverse=True)
