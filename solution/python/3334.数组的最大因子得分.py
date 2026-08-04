from math import gcd


class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)

        def lcm(first: int, second: int) -> int:
            if first == 0:
                return second
            if second == 0:
                return first
            return first // gcd(first, second) * second

        prefix_gcd = [0] * (n + 1)
        prefix_lcm = [0] * (n + 1)
        for index, value in enumerate(nums):
            prefix_gcd[index + 1] = gcd(prefix_gcd[index], value)
            prefix_lcm[index + 1] = lcm(prefix_lcm[index], value)

        suffix_gcd = [0] * (n + 1)
        suffix_lcm = [0] * (n + 1)
        for index in range(n - 1, -1, -1):
            suffix_gcd[index] = gcd(suffix_gcd[index + 1], nums[index])
            suffix_lcm[index] = lcm(suffix_lcm[index + 1], nums[index])

        answer = 0
        for index in range(n):
            combined_gcd = gcd(prefix_gcd[index], suffix_gcd[index + 1])
            combined_lcm = lcm(prefix_lcm[index], suffix_lcm[index + 1])
            answer = max(answer, combined_gcd * combined_lcm)
        return max(answer, prefix_gcd[n] * prefix_lcm[n])


if __name__ == "__main__":
    test_cases = [
        (([2, 4, 8, 16],), 64),
        (([1, 2, 3, 4, 5],), 60),
        (([3],), 9),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maxScore(nums) == expected
