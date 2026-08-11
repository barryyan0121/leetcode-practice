from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        left = answer = 0
        for right, value in enumerate(nums2):
            while left < len(nums1) and left <= right and nums1[left] > value:
                left += 1
            if left <= right:
                answer = max(answer, right - left)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]) == 2
    print("1855 passed")
