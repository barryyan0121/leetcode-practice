"""1966. 未排序数组中的可被二分查找的数"""


class Solution:
    def binarySearchableNumbers(self, nums: list[int]) -> int:
        answer = 0
        maximum = float("-inf")
        suffix_min = [0] * len(nums)
        current = float("inf")
        for i in range(len(nums) - 1, -1, -1):
            current = min(current, nums[i])
            suffix_min[i] = current
        for i, value in enumerate(nums):
            maximum = max(maximum, value)
            answer += maximum == value == suffix_min[i]
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 3, 2],), 1), (([3, 2, 1],), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().binarySearchableNumbers(*args) == expected
