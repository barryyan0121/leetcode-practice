class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        minimum_prefix = {}
        prefix = 0
        answer = None
        for number in nums:
            prefix += number
            for endpoint in (number - k, number + k):
                if endpoint in minimum_prefix:
                    candidate = prefix - minimum_prefix[endpoint]
                    answer = candidate if answer is None else max(answer, candidate)
            start_prefix = prefix - number
            minimum_prefix[number] = min(
                minimum_prefix.get(number, start_prefix), start_prefix
            )
        return answer if answer is not None else 0


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5, 6], 1), 11),
        (([-1, 3, 2, 4, 5], 3), 11),
        (([-1, -2, -3, -4], 2), -6),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().maximumSubarraySum(nums, k) == expected
