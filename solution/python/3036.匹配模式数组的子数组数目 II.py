class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        target = pattern
        prefix = [0] * len(target)
        matched = 0
        for index in range(1, len(target)):
            while matched and target[index] != target[matched]:
                matched = prefix[matched - 1]
            matched += target[index] == target[matched]
            prefix[index] = matched

        answer = 0
        matched = 0
        for left in range(len(nums) - 1):
            comparison = (nums[left + 1] > nums[left]) - (nums[left + 1] < nums[left])
            while matched and comparison != target[matched]:
                matched = prefix[matched - 1]
            matched += comparison == target[matched]
            if matched == len(target):
                answer += 1
                matched = prefix[matched - 1]
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5, 6], [1, 1]), 4),
        (([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1]), 2),
    ]
    for _, ((nums, pattern), expected) in enumerate(test_cases):
        assert Solution().countMatchingSubarrays(nums, pattern) == expected
