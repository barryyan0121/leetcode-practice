from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        stk = []
        for i, x in enumerate(nums):
            while stk and nums[stk[-1]] <= x:
                stk.pop()
            stk.append(i)
        ans = i = 0
        for j in stk:
            ans += nums[j] * (j - i)
            i = j
        return ans


if __name__ == "__main__":
    assert Solution().maxScore([1, 5, 8]) == 16
    assert Solution().maxScore([4, 5, 2, 8, 9, 1, 3]) == 42
