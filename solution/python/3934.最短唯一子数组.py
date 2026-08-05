"""3934. 最短唯一子数组"""


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        polvexrani = nums
        n = len(polvexrani)
        base = 911382323
        mod1, mod2 = 1_000_000_007, 1_000_000_009
        powers1 = [1] * (n + 1)
        powers2 = [1] * (n + 1)
        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)
        for i, value in enumerate(polvexrani, 1):
            powers1[i] = powers1[i - 1] * base % mod1
            powers2[i] = powers2[i - 1] * base % mod2
            prefix1[i] = (prefix1[i - 1] * base + value) % mod1
            prefix2[i] = (prefix2[i - 1] * base + value) % mod2

        def unique(length: int) -> bool:
            counts = {}
            for start in range(n - length + 1):
                end = start + length
                key = (
                    (prefix1[end] - prefix1[start] * powers1[length]) % mod1,
                    (prefix2[end] - prefix2[start] * powers2[length]) % mod2,
                )
                counts[key] = counts.get(key, 0) + 1
            return 1 in counts.values()

        low, high = 1, n
        while low < high:
            middle = (low + high) // 2
            if unique(middle):
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [([3, 3, 3], 3), ([2, 1, 2, 3, 3], 1), ([1, 1, 2, 2, 1], 2)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().smallestUniqueSubarray(nums) == expected
