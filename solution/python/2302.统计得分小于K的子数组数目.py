"""2302. 统计得分小于 K 的子数组数目"""


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        answer = left = total = 0
        for right, value in enumerate(nums):
            total += value
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            answer += right - left + 1
        return answer
