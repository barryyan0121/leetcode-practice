class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        position = 0
        answer = 0
        for move in nums:
            position += move
            answer += position == 0
        return answer


if __name__ == "__main__":
    test_cases = [([2, 3, -5], 1), ([3, 2, -3, -2, -1], 1)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().returnToBoundaryCount(nums) == expected
