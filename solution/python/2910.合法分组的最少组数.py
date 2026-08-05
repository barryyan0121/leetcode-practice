"""2910. 合法分组的最少组数"""

from collections import Counter


class Solution:
    def minGroupsForValidAssignment(self, nums: list[int]) -> int:
        frequencies = Counter(Counter(nums).values())
        minimum = min(frequencies)
        answer = len(nums)
        for size in range(1, minimum + 1):
            groups = 0
            possible = True
            for frequency in frequencies:
                quotient, remainder = divmod(frequency, size + 1)
                if remainder and size - remainder > quotient:
                    possible = False
                    break
                groups += quotient + bool(remainder)
            if possible:
                answer = min(answer, groups)
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 2, 3, 2, 3],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minGroupsForValidAssignment(*args) == expected
