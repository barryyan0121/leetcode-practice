class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        end = 1
        while end < len(nums) and nums[end] == nums[end - 1] + 1:
            end += 1
        answer = sum(nums[:end])
        values = set(nums)
        while answer in values:
            answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 2, 5],), 6),
        (([3, 4, 5, 1, 12],), 13),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().missingInteger(nums) == expected
