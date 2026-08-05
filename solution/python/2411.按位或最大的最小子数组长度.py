"""2411. 按位或最大的最小子数组长度"""


class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        last = [-1] * 31
        answer = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for bit in range(31):
                if nums[i] >> bit & 1:
                    last[bit] = i
            answer[i] = max(i, max(last)) - i + 1
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 0, 2, 1, 3],), [3, 3, 2, 2, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().smallestSubarrays(*args) == expected
