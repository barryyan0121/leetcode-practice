class Solution:
    def maximumSumSubsequence(self, nums: list[int], queries: list[list[int]]) -> int:
        modulo = 10**9 + 7
        negative = -(10**18)
        size = 1
        while size < len(nums):
            size <<= 1
        tree = [[[0, 0], [0, negative]] for _ in range(2 * size)]

        def make_leaf(value: int) -> list[list[int]]:
            return [[0, value], [0, negative]]

        def merge(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
            return [
                [
                    max(
                        left[row][0] + right[0][column], left[row][1] + right[1][column]
                    )
                    for column in range(2)
                ]
                for row in range(2)
            ]

        for index, value in enumerate(nums):
            tree[size + index] = make_leaf(value)
        for index in range(size - 1, 0, -1):
            tree[index] = merge(tree[index * 2], tree[index * 2 + 1])

        answer = 0
        for position, value in queries:
            index = size + position
            tree[index] = make_leaf(value)
            index >>= 1
            while index:
                tree[index] = merge(tree[index * 2], tree[index * 2 + 1])
                index >>= 1
            answer += max(tree[1][0])
        return answer % modulo


if __name__ == "__main__":
    test_cases = [
        ([3, 5, 9], [[1, -2], [0, -1]], 21),
        ([-1, -2], [[0, 3]], 3),
    ]
    for _, (nums, queries, expected) in enumerate(test_cases):
        assert Solution().maximumSumSubsequence(nums, queries) == expected
