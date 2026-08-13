class Solution:
    def numberOfGoodPartitions(self, nums: list[int]) -> int:
        last = {value: index for index, value in enumerate(nums)}
        groups = right = 0
        for index, value in enumerate(nums):
            right = max(right, last[value])
            if index == right:
                groups += 1
        return pow(2, groups - 1, 10**9 + 7)


if __name__ == "__main__":
    solution = Solution()
    assert solution.numberOfGoodPartitions([1, 2, 3, 4]) == 8
    assert solution.numberOfGoodPartitions([1, 1, 1, 1]) == 1
    assert solution.numberOfGoodPartitions([1, 2, 1, 3]) == 2
