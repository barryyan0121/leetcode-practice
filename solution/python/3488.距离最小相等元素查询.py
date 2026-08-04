"""3488. 距离最小相等元素查询"""

from bisect import bisect_left


class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        positions = {}
        for index, value in enumerate(nums):
            positions.setdefault(value, []).append(index)
        size = len(nums)
        answer = []
        for query in queries:
            indices = positions[nums[query]]
            if len(indices) == 1:
                answer.append(-1)
                continue
            offset = bisect_left(indices, query)
            previous = indices[offset - 1]
            following = indices[(offset + 1) % len(indices)]
            answer.append(
                min(
                    (query - previous) % size,
                    (following - query) % size,
                )
            )
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]), [2, -1, 3]),
        (([1, 2, 3, 4], [0, 1, 2, 3]), [-1, -1, -1, -1]),
    ]
    for _, ((nums, queries), expected) in enumerate(test_cases):
        assert Solution().solveQueries(nums, queries) == expected
