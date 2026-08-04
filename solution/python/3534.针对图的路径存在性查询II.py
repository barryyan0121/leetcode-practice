"""3534. 针对图的路径存在性查询 II"""

from bisect import bisect_right


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[int]:
        order = sorted(range(n), key=nums.__getitem__)
        values = [nums[index] for index in order]
        rank = [0] * n
        for position, index in enumerate(order):
            rank[index] = position

        next_position = [bisect_right(values, value + maxDiff) - 1 for value in values]
        levels = [next_position]
        log = n.bit_length()
        for _ in range(1, log):
            previous = levels[-1]
            levels.append([previous[previous[i]] for i in range(n)])

        def distance(start: int, target: int) -> int:
            if start == target:
                return 0
            if next_position[start] == start:
                return -1
            current = start
            steps = 0
            for level in range(log - 1, -1, -1):
                candidate = levels[level][current]
                if candidate < target and candidate != current:
                    current = candidate
                    steps += 1 << level
            return steps + 1 if levels[0][current] >= target else -1

        answer = []
        for source, target in queries:
            left, right = rank[source], rank[target]
            if left > right:
                left, right = right, left
            answer.append(distance(left, right))
        return answer


if __name__ == "__main__":
    test_cases = [
        ((5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4]]), [1, 1]),
        ((5, [5, 3, 1, 9, 10], 2, [[0, 1], [0, 2], [2, 3], [4, 3]]), [1, 2, -1, 1]),
    ]
    for _, ((n, nums, max_diff, queries), expected) in enumerate(test_cases):
        assert Solution().pathExistenceQueries(n, nums, max_diff, queries) == expected
