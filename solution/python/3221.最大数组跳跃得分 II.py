class Solution:
    def maxScore(self, nums: list[int]) -> int:
        maximum = answer = 0
        for value in nums[:0:-1]:
            maximum = max(maximum, value)
            answer += maximum
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 5, 8],), 16), (([4, 5, 2, 8, 9, 1, 3],), 42)]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maxScore(nums) == expected
