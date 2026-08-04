class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        runs = []
        length = 1
        for index in range(1, len(nums)):
            if nums[index - 1] < nums[index]:
                length += 1
            else:
                runs.append(length)
                length = 1
        runs.append(length)

        answer = 0
        for index, length in enumerate(runs):
            answer = max(answer, length // 2)
            if index:
                answer = max(answer, min(runs[index - 1], length))
        return answer


if __name__ == "__main__":
    test_cases = [
        (([2, 5, 7, 8, 9, 2, 3, 4, 3, 1],), 3),
        (([1, 2, 3, 4, 4, 4, 4, 5, 6, 7],), 2),
        (([1, 2, 3, 4],), 2),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maxIncreasingSubarrays(nums) == expected
