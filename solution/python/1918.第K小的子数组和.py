"""1918. 第 K 小的子数组和"""


class Solution:
    def kthSmallestSubarraySum(self, nums: list[int], k: int) -> int:
        def count(limit: int) -> int:
            total = 0
            left = 0
            answer = 0
            for right, value in enumerate(nums):
                total += value
                while total > limit:
                    total -= nums[left]
                    left += 1
                answer += right - left + 1
            return answer

        low, high = min(nums), sum(nums)
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [(([2, 1, 3], 4), 3), (([1, 2, 3, 4], 10), 10)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().kthSmallestSubarraySum(*args) == expected
