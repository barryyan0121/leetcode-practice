class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        increasing = 1
        answer = []
        for index, value in enumerate(nums):
            if index and value == nums[index - 1] + 1:
                increasing += 1
            else:
                increasing = 1
            if index >= k - 1:
                answer.append(value if increasing >= k else -1)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 3, 2, 5], 3), [3, 4, -1, -1, -1]),
        (([2, 2, 2, 2, 2], 4), [-1, -1]),
        (([3, 2, 3, 2, 3, 2], 2), [-1, 3, -1, 3, -1]),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().resultsArray(nums, k) == expected
