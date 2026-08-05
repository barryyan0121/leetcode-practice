from collections import deque


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        lo, hi = deque(), deque()
        left = ans = 0
        for right, value in enumerate(nums):
            while lo and nums[lo[-1]] > value:
                lo.pop()
            while hi and nums[hi[-1]] < value:
                hi.pop()
            lo.append(right)
            hi.append(right)
            while nums[hi[0]] - nums[lo[0]] > 2:
                left += 1
                if lo[0] < left:
                    lo.popleft()
                if hi[0] < left:
                    hi.popleft()
            ans += right - left + 1
        return ans


if __name__ == "__main__":
    assert Solution().continuousSubarrays([5, 4, 2, 4]) == 8
