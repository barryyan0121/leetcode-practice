from collections import deque
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum, minimum = deque(), deque()
        answer = left = 0
        for right, value in enumerate(nums):
            while maximum and nums[maximum[-1]] <= value:
                maximum.pop()
            maximum.append(right)
            while minimum and nums[minimum[-1]] >= value:
                minimum.pop()
            minimum.append(right)
            while (nums[maximum[0]] - nums[minimum[0]]) * (right - left + 1) > k:
                left += 1
                if maximum[0] < left:
                    maximum.popleft()
                if minimum[0] < left:
                    minimum.popleft()
            answer += right - left + 1
        return answer


if __name__ == "__main__":
    assert Solution().countSubarrays([1, 2, 3], 3) == 5
