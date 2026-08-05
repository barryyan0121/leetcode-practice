"""3583. 统计特殊三元组"""

from collections import Counter


class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        right = Counter(nums)
        left = Counter()
        answer = 0
        for value in nums:
            right[value] -= 1
            target = value * 2
            answer = (answer + left[target] * right[target]) % mod
            left[value] += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (([6, 3, 6],), 1),
        (([0, 1, 0, 0],), 1),
        (([8, 4, 2, 8, 4],), 2),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().specialTriplets(nums) == expected
