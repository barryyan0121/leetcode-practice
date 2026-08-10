"""2461. 长度为 K 的子数组的最大和"""


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        counts = {}
        total = answer = 0
        for right, value in enumerate(nums):
            total += value
            counts[value] = counts.get(value, 0) + 1
            if right >= k:
                left_value = nums[right - k]
                total -= left_value
                counts[left_value] -= 1
                if counts[left_value] == 0:
                    del counts[left_value]
            if right >= k - 1 and len(counts) == k:
                answer = max(answer, total)
        return answer
