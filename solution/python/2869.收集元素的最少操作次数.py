"""2869. 收集元素的最少操作次数"""


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        found = set()
        for index in range(len(nums) - 1, -1, -1):
            found.add(nums[index])
            if all(value in found for value in range(1, k + 1)):
                return len(nums) - index
        return len(nums)


if __name__ == "__main__":
    assert Solution().minOperations([3, 1, 5, 4, 2], 2) == 4
