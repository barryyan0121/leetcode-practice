"""3027. 人员站位的方案数 II"""


class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        ordered = sorted(points, key=lambda point: (point[0], -point[1]))
        answer = 0
        for index, (_, top) in enumerate(ordered):
            lower_bound = -(10**19)
            for next_index in range(index + 1, len(ordered)):
                _, bottom = ordered[next_index]
                if bottom <= top and bottom > lower_bound:
                    answer += 1
                    lower_bound = bottom
        return answer


if __name__ == "__main__":
    test_cases = [
        ([[1, 1], [2, 2], [3, 3]], 0),
        ([[6, 2], [4, 4], [2, 6]], 2),
        ([[3, 1], [1, 3], [1, 1]], 2),
        ([[1, 4], [2, 3], [3, 2], [4, 1]], 3),
    ]
    for _, (points, expected) in enumerate(test_cases):
        assert Solution().numberOfPairs(points) == expected
