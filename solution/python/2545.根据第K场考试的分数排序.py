"""2545. 根据第 K 场考试的分数排序"""


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=lambda row: row[k], reverse=True)


if __name__ == "__main__":
    test_cases = [
        (
            ([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2),
            [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]],
        )
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().sortTheStudents(*args) == expected
