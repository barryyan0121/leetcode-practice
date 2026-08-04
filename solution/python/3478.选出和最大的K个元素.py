"""3478. 选出和最大的 K 个元素"""

import heapq


class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        order = sorted(range(len(nums1)), key=lambda i: nums1[i])
        answer = [0] * len(nums1)
        top_values = []
        top_sum = 0
        start = 0
        while start < len(order):
            end = start
            while end < len(order) and nums1[order[end]] == nums1[order[start]]:
                end += 1
            for pos in range(start, end):
                answer[order[pos]] = top_sum
            for pos in range(start, end):
                value = nums2[order[pos]]
                heapq.heappush(top_values, value)
                top_sum += value
                if len(top_values) > k:
                    top_sum -= heapq.heappop(top_values)
            start = end
        return answer


if __name__ == "__main__":
    test_cases = [
        (([4, 2, 1, 5, 3], [10, 20, 30, 40, 50], 2), [80, 30, 0, 80, 50]),
        (([2, 2, 2, 2], [3, 1, 2, 3], 1), [0, 0, 0, 0]),
    ]
    for _, ((nums1, nums2, k), expected) in enumerate(test_cases):
        assert Solution().findMaxSum(nums1, nums2, k) == expected
