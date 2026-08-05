class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        a, b = nums.index(1), nums.index(len(nums))
        return a + len(nums) - 1 - b - (a > b)


if __name__ == "__main__":
    assert Solution().semiOrderedPermutation([2, 1, 4, 3]) == 2
