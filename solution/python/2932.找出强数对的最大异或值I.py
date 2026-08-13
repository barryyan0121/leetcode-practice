class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        answer = 0
        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    answer = max(answer, x ^ y)
        return answer


assert Solution().maximumStrongPairXor([1, 2, 3, 4, 5]) == 7
