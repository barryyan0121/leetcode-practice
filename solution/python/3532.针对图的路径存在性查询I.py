"""3532. 针对图的路径存在性查询 I"""


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[bool]:
        component = [0] * n
        for i in range(1, n):
            component[i] = component[i - 1] + (nums[i] - nums[i - 1] > maxDiff)
        return [component[u] == component[v] for u, v in queries]


if __name__ == "__main__":
    test_cases = [
        ((3, [1, 3, 5], 2, [[0, 1], [0, 2]]), [True, True]),
        ((4, [1, 5, 6, 10], 1, [[0, 1], [1, 2], [0, 3]]), [False, True, False]),
    ]
    for _, ((n, nums, max_diff, queries), expected) in enumerate(test_cases):
        assert Solution().pathExistenceQueries(n, nums, max_diff, queries) == expected
