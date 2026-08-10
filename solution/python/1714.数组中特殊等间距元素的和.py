from collections import defaultdict
from math import isqrt


class Solution:
    def solve(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        mod = 10**9 + 7
        threshold = isqrt(len(nums)) + 1
        answer = [0] * len(queries)
        small = defaultdict(list)
        for index, (start, step) in enumerate(queries):
            if step <= threshold:
                small[step].append((index, start))
            else:
                total = 0
                for position in range(start, len(nums), step):
                    total += nums[position]
                answer[index] = total % mod
        for step, grouped in small.items():
            suffix = [0] * (len(nums) + step)
            for position in range(len(nums) - 1, -1, -1):
                suffix[position] = nums[position] + suffix[position + step]
            for index, start in grouped:
                answer[index] = suffix[start] % mod
        return answer


if __name__ == "__main__":
    test_cases = [
        (([0, 1, 2, 3, 4, 5, 6, 7], [[0, 3], [5, 1], [4, 2]]), [9, 18, 10]),
        (([100, 200, 101, 201, 102, 202, 103, 203], [[0, 7]]), [303]),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().solve(*args) == expected, index
