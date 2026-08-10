"""2871. 将数组分成最多数目的子数组"""


class Solution:
    def maxSubarrays(self, nums: list[int]) -> int:
        current = (1 << 31) - 1
        answer = 0
        for value in nums:
            current &= value
            if current == 0:
                answer += 1
                current = (1 << 31) - 1
        return answer or 1


if __name__ == "__main__":
    assert Solution().maxSubarrays([1, 0, 2, 0, 1, 2]) == 3
