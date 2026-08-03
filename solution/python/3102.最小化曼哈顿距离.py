class Solution:
    def minimumDistance(self, points: list[list[int]]) -> int:
        transformed = [(x + y, x - y) for x, y in points]
        candidates = set()
        for coordinate in range(2):
            order = sorted(range(len(points)), key=lambda i: transformed[i][coordinate])
            candidates.update(order[:2])
            candidates.update(order[-2:])

        answer = float("inf")
        for removed in candidates:
            remaining = [i for i in range(len(points)) if i != removed]
            maximum = max(
                max(transformed[i][0] for i in remaining)
                - min(transformed[i][0] for i in remaining),
                max(transformed[i][1] for i in remaining)
                - min(transformed[i][1] for i in remaining),
            )
            answer = min(answer, maximum)
        return answer


if __name__ == "__main__":
    test_cases = [
        ([[3, 10], [5, 15], [10, 2], [4, 4]], 12),
        ([[1, 1], [1, 2], [1, 3]], 1),
    ]
    for _, (points, expected) in enumerate(test_cases):
        assert Solution().minimumDistance(points) == expected
