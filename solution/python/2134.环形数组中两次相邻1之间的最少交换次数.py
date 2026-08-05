"""2134. 环形数组中两次相邻 1 之间的最少交换次数"""


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        ones = sum(nums)
        if ones <= 1:
            return 0
        doubled = nums * 2
        window = sum(doubled[:ones])
        answer = ones - window
        for right in range(ones, len(nums) + ones):
            window += doubled[right] - doubled[right - ones]
            answer = min(answer, ones - window)
        return answer


if __name__ == "__main__":
    test_cases = [(([0, 1, 0, 1, 1, 0, 0],), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minSwaps(*args) == expected
