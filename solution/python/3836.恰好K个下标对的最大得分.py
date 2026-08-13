from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        neg_inf = -10**30
        dp = [[0] + [neg_inf] * k for _ in range(len(nums2) + 1)]
        for a in nums1:
            current = [[0] + [neg_inf] * k for _ in range(len(nums2) + 1)]
            for j in range(1, len(nums2) + 1):
                for count in range(1, min(k, j) + 1):
                    current[j][count] = max(
                        dp[j][count],
                        current[j - 1][count],
                        dp[j - 1][count - 1] + a * nums2[j - 1],
                    )
            dp = current
        return dp[-1][k]


if __name__ == "__main__":
    assert Solution().maxScore([1, 2, 3], [4, 5, 6], 2) == 28
