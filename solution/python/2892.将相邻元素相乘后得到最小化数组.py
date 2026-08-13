class Solution:
    def minArrayLength(self, nums: list[int], k: int) -> int:
        if 0 in nums:
            return 1
        answer = 1
        product = 1
        for number in nums:
            if product * number > k:
                answer += 1
                product = number
            else:
                product *= number
        return answer


assert Solution().minArrayLength([2, 3, 3, 7, 3, 5], 20) == 3
assert Solution().minArrayLength([3, 3, 3, 3], 6) == 4
