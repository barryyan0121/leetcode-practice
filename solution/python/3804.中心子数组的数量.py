from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        answer = 0
        for left in range(len(nums)):
            total = 0
            values = set()
            for right in range(left, len(nums)):
                total += nums[right]
                values.add(nums[right])
                answer += total in values
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.centeredSubarrays([-1, 1, 0]) == 5
    assert s.centeredSubarrays([2, -3]) == 2
