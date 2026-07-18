from collections import defaultdict


class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        scores = defaultdict(list)
        for student_id, score in items:
            scores[student_id].append(score)
        return [
            [student_id, sum(sorted(scores[student_id], reverse=True)[:5]) // 5]
            for student_id in sorted(scores)
        ]


if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 91],
                [1, 92],
                [2, 93],
                [2, 97],
                [1, 60],
                [2, 77],
                [1, 65],
                [1, 87],
                [1, 100],
                [2, 100],
                [2, 76],
            ],
            [[1, 87], [2, 88]],
        ),
        (
            [
                [2, 1],
                [1, 100],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [2, 2],
                [2, 3],
                [2, 4],
                [2, 5],
            ],
            [[1, 20], [2, 3]],
        ),
    ]
    for _, (items, expected) in enumerate(test_cases):
        assert Solution().highFive(items) == expected
