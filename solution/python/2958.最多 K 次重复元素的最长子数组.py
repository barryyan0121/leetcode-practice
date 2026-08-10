"""2958. 最多 K 次重复元素的最长子数组"""

from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        left = answer = 0
        for right, value in enumerate(nums):
            counts[value] += 1
            while counts[value] > k:
                counts[nums[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    assert Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6
