class Solution:
    def maximumPossibleSize(self, nums: list[int]) -> int:
        answer = 0
        maximum = 0
        for value in nums:
            if value >= maximum:
                answer += 1
                maximum = value
        return answer


if __name__ == "__main__":
    test_cases = [(([4, 2, 5, 3, 5],), 3), (([1, 2, 3],), 3)]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maximumPossibleSize(nums) == expected
