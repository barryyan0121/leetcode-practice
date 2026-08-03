from collections import Counter


class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        frequencies = Counter(nums1)
        multipliers = Counter(nums2)
        maximum = max(nums1)
        answer = 0
        for value, frequency in multipliers.items():
            divisor = value * k
            if divisor == 0:
                continue
            for multiple in range(divisor, maximum + 1, divisor):
                answer += frequencies[multiple] * frequency
        return answer


if __name__ == "__main__":
    test_cases = [([1, 3, 4], [1, 3], 1, 4), ([1, 2, 4], [2, 4], 1, 3)]
    for _, (nums1, nums2, k, expected) in enumerate(test_cases):
        assert Solution().numberOfPairs(nums1, nums2, k) == expected
