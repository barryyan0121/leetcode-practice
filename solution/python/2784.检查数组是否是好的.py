class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        return len(nums) == n + 1 and sorted(nums) == list(range(1, n + 1)) + [n]


if __name__ == "__main__":
    assert Solution().isGood([1, 3, 3, 2]) is True
