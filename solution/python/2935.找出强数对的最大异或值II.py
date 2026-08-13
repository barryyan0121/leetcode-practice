class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        nums.sort()
        answer = 0
        for i, x in enumerate(nums):
            for y in nums[i:]:
                if y > 2 * x:
                    break
                answer = max(answer, x ^ y)
        return answer


assert Solution().maximumStrongPairXor([1, 2, 3, 4, 5]) == 7
