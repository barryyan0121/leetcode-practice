"""2226. 每个小孩最多能分到多少糖果"""


class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left, right = 0, sum(candies) // k
        while left < right:
            mid = (left + right + 1) // 2
            if sum(value // mid for value in candies) >= k:
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    assert Solution().maximumCandies([5, 8, 6], 3) == 5
