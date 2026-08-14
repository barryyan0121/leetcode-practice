class Solution:
    def orArray(self, nums: list[int]) -> list[int]:
        return [a | b for a, b in zip(nums, nums[1:])]


if __name__ == "__main__":
    assert Solution().orArray([1, 2, 4, 8]) == [3, 6, 12]
