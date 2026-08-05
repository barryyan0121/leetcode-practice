"""2447. 最大公因数等于 K 的子数组数目"""

from math import gcd


class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        answer = 0
        for start in range(len(nums)):
            current = 0
            for value in nums[start:]:
                current = gcd(current, value)
                if current == k:
                    answer += 1
                elif current < k or current % k:
                    break
        return answer


if __name__ == "__main__":
    test_cases = [(([9, 3, 1, 2, 6, 3], 3), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().subarrayGCD(*args) == expected
