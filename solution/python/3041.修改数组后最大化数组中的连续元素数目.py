from collections import defaultdict


class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        best_ending = defaultdict(int)
        answer = 0
        for number in sorted(nums):
            previous = best_ending[number]
            best_ending[number] = max(best_ending[number], best_ending[number - 1] + 1)
            best_ending[number + 1] = max(best_ending[number + 1], previous + 1)
            answer = max(answer, best_ending[number], best_ending[number + 1])
        return answer


if __name__ == "__main__":
    test_cases = [([2, 1, 5, 1, 1], 3), ([1, 4, 7, 10], 1)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maxSelectedElements(nums) == expected
