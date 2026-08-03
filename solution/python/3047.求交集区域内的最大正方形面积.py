class Solution:
    def largestSquareArea(
        self, bottomLeft: list[list[int]], topRight: list[list[int]]
    ) -> int:
        answer = 0
        for first in range(len(bottomLeft)):
            for second in range(first + 1, len(bottomLeft)):
                width = min(topRight[first][0], topRight[second][0]) - max(
                    bottomLeft[first][0], bottomLeft[second][0]
                )
                height = min(topRight[first][1], topRight[second][1]) - max(
                    bottomLeft[first][1], bottomLeft[second][1]
                )
                answer = max(answer, max(0, min(width, height)) ** 2)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]]), 1),
        (([[1, 1], [3, 3], [3, 1]], [[2, 2], [4, 4], [4, 2]]), 0),
    ]
    for _, ((bottom_left, top_right), expected) in enumerate(test_cases):
        assert Solution().largestSquareArea(bottom_left, top_right) == expected
