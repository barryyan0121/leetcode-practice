from collections import Counter
from math import gcd


class Solution:
    def numberOfSubsequences(self, nums: list[int]) -> int:
        size = len(nums)
        right = Counter()
        for r in range(4, size - 2):
            for s in range(r + 2, size):
                divisor = gcd(nums[s], nums[r])
                right[(nums[s] // divisor, nums[r] // divisor)] += 1

        answer = 0
        for q in range(2, size - 4):
            left = Counter()
            for p in range(q - 1):
                divisor = gcd(nums[p], nums[q])
                left[(nums[p] // divisor, nums[q] // divisor)] += 1
            answer += sum(count * right[key] for key, count in left.items())

            r = q + 2
            for s in range(r + 2, size):
                divisor = gcd(nums[s], nums[r])
                key = (nums[s] // divisor, nums[r] // divisor)
                right[key] -= 1
                if right[key] == 0:
                    del right[key]
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 3, 6, 1],), 1),
        (([3, 4, 3, 4, 3, 4, 3, 4],), 3),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().numberOfSubsequences(nums) == expected
