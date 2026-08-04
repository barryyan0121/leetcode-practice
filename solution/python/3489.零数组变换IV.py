"""3489. 零数组变换 IV"""


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        varmelistra = (nums, queries)
        reachable = [1] * len(nums)
        if all(value == 0 for value in nums):
            return 0
        for query_index, (left, right, value) in enumerate(queries, 1):
            for index in range(left, right + 1):
                reachable[index] |= reachable[index] << value
                reachable[index] &= (1 << (nums[index] + 1)) - 1
            if all(reachable[index] & (1 << nums[index]) for index in range(len(nums))):
                return query_index
        return -1


if __name__ == "__main__":
    test_cases = [
        (([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]), 2),
        (([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]]), -1),
        (([1, 2, 3, 2, 1], [[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1]]), 4),
    ]
    for _, ((nums, queries), expected) in enumerate(test_cases):
        assert Solution().minZeroArray(nums, queries) == expected
