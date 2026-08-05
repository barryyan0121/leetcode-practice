from functools import lru_cache


class Solution:
    def concatenatedDivisibility(self, nums: list[int], k: int) -> list[int]:
        nums.sort()
        lengths = [len(str(value)) for value in nums]
        powers = [10**length % k for length in lengths]

        @lru_cache(None)
        def possible(mask: int, remainder: int) -> bool:
            if mask == (1 << len(nums)) - 1:
                return remainder == 0
            for index, value in enumerate(nums):
                if not mask >> index & 1:
                    next_remainder = (remainder * powers[index] + value) % k
                    if possible(mask | (1 << index), next_remainder):
                        return True
            return False

        if not possible(0, 0):
            return []
        answer = []
        mask = remainder = 0
        while mask != (1 << len(nums)) - 1:
            for index, value in enumerate(nums):
                if mask >> index & 1:
                    continue
                next_remainder = (remainder * powers[index] + value) % k
                if possible(mask | (1 << index), next_remainder):
                    answer.append(value)
                    mask |= 1 << index
                    remainder = next_remainder
                    break
        return answer


if __name__ == "__main__":
    test_cases = [
        (([3, 12, 45], 5), [3, 12, 45]),
        (([10, 5], 10), [5, 10]),
        (([1, 2, 3], 5), []),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().concatenatedDivisibility(nums, k) == expected
