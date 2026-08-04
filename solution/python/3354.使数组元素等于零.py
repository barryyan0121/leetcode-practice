class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        answer = 0
        for value in nums:
            if value == 0:
                difference = abs(left - (total - left))
                if difference == 0:
                    answer += 2
                elif difference == 1:
                    answer += 1
            left += value
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 0, 2, 0, 3],), 2),
        (([2, 3, 4, 0, 4, 1, 0],), 0),
        (([1, 0, 1],), 2),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().countValidSelections(nums) == expected
