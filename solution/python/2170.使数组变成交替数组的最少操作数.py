"""2170. 使数组变成交替数组的最少操作数"""

from collections import Counter


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        even = Counter(nums[::2]).most_common(2)
        odd = Counter(nums[1::2]).most_common(2)
        candidates = []
        for even_value, even_count in even + [(None, 0)]:
            for odd_value, odd_count in odd + [(None, 0)]:
                if even_value != odd_value:
                    candidates.append(len(nums) - even_count - odd_count)
        return min(candidates)


if __name__ == "__main__":
    test_cases = [(([3, 1, 3, 2, 4, 3],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumOperations(*args) == expected
