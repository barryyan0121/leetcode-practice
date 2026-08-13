class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        return max(nums.count(0), nums.count(1), 1)


if __name__ == "__main__":
    assert Solution().maximumLength([1, 2, 3, 4]) == 1
    assert Solution().maximumLength([1, 2, 1, 1, 2, 1]) == 4
