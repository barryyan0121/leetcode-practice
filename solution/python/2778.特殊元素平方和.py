class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        return sum(value * value for i, value in enumerate(nums, 1) if n % i == 0)


if __name__ == "__main__":
    assert Solution().sumOfSquares([1, 2, 3, 4]) == 21
