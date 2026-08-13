from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])
        prefix = 0
        answer = -(10**30)
        for i, x in enumerate(nums[:-1]):
            prefix += x
            answer = max(answer, prefix - suffix[i + 1])
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.maximumScore([10, -1, 3, -4, -5]) == 17
    assert s.maximumScore([-7, -5, 3]) == -2
    assert s.maximumScore([1, 1]) == 0
