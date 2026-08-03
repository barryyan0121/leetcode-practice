from functools import cache


class Solution:
    def findPermutation(self, nums: list[int]) -> list[int]:
        size = len(nums)
        full = (1 << size) - 1

        @cache
        def best(mask: int, last: int) -> int:
            if mask == full:
                return abs(last - nums[0])
            answer = 10**18
            for candidate in range(1, size):
                if not mask >> candidate & 1:
                    answer = min(
                        answer,
                        abs(last - nums[candidate])
                        + best(mask | (1 << candidate), candidate),
                    )
            return answer

        permutation = [0]
        mask = 1
        last = 0
        while mask != full:
            target = best(mask, last)
            for candidate in range(1, size):
                if not mask >> candidate & 1:
                    cost = abs(last - nums[candidate]) + best(
                        mask | (1 << candidate), candidate
                    )
                    if cost == target:
                        permutation.append(candidate)
                        mask |= 1 << candidate
                        last = candidate
                        break
        return permutation


if __name__ == "__main__":
    test_cases = [([1, 0, 2], [0, 1, 2]), ([2, 0, 1], [0, 1, 2])]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().findPermutation(nums) == expected
