from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        suffix = 0
        answer = 0
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1 and nums[i] * (len(nums) - i - 1) > suffix:
                answer += 1
            suffix += nums[i]
        return answer


if __name__ == "__main__":
    assert Solution().dominantIndices([5, 4, 3]) == 2
