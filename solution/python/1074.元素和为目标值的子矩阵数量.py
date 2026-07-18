from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows, columns = len(matrix), len(matrix[0])
        answer = 0
        for left in range(columns):
            sums = [0] * rows
            for right in range(left, columns):
                prefix = 0
                counts = defaultdict(int, {0: 1})
                for row in range(rows):
                    sums[row] += matrix[row][right]
                    prefix += sums[row]
                    answer += counts[prefix - target]
                    counts[prefix] += 1
        return answer


if __name__ == "__main__":
    test_cases = [([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0, 4), ([[1, -1], [-1, 1]], 0, 5)]
    for _, (matrix, target, expected) in enumerate(test_cases):
        assert Solution().numSubmatrixSumTarget(matrix, target) == expected
