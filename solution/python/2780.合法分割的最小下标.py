class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        candidate = count = 0
        for value in nums:
            if count == 0:
                candidate = value
            count += 1 if value == candidate else -1
        total = nums.count(candidate)
        left = 0
        for i, value in enumerate(nums[:-1]):
            left += value == candidate
            if left * 2 > i + 1 and (total - left) * 2 > len(nums) - i - 1:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().minimumIndex([1, 2, 2, 2]) == 2
