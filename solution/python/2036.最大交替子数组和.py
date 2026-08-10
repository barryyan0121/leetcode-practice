"""2036. 最大交替子数组和"""


class Solution:
    def maximumAlternatingSubarraySum(self, nums: list[int]) -> int:
        answer = float("-inf")
        for start_parity in (0, 1):
            current = float("-inf")
            for index, value in enumerate(nums):
                signed = value if (index - start_parity) % 2 == 0 else -value
                if index % 2 == start_parity:
                    current = max(signed, current + signed)
                else:
                    current += signed
                answer = max(answer, current)
        return answer


if __name__ == "__main__":
    test_cases = [(([3, -1, 1, 2],), 5), (([2, 2, 2, 2, 2],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumAlternatingSubarraySum(*args) == expected
