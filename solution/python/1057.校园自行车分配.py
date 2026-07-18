class Solution:
    def assignBikes(
        self, workers: list[list[int]], bikes: list[list[int]]
    ) -> list[int]:
        pairs = sorted(
            (abs(x - a) + abs(y - b), i, j)
            for i, (x, y) in enumerate(workers)
            for j, (a, b) in enumerate(bikes)
        )
        answer = [-1] * len(workers)
        used = set()
        for _, i, j in pairs:
            if answer[i] < 0 and j not in used:
                answer[i] = j
                used.add(j)
        return answer


if __name__ == "__main__":
    test_cases = [([[0, 0], [2, 1]], [[1, 2], [3, 3]], [1, 0])]
    for _, (workers, bikes, expected) in enumerate(test_cases):
        assert Solution().assignBikes(workers, bikes) == expected
