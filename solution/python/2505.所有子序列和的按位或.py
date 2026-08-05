"""2505. 所有子序列和的按位或"""


class Solution:
    def subsequenceSumOr(self, nums: list[int]) -> int:
        answer = 0
        lower_sum = 0
        for bit in range(31):
            mask = (1 << bit) - 1
            if any(value >> bit & 1 for value in nums) or lower_sum >= 1 << bit:
                answer |= 1 << bit
            lower_sum += sum(value & mask for value in nums)
        return answer


if __name__ == "__main__":
    test_cases = [(([2, 1, 0, 3],), 7), (([0, 0, 0],), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().subsequenceSumOr(*args) == expected
