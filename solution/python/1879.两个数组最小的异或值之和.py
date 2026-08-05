"""1879. 两个数组最小的异或值之和"""


class Solution:
    def minimumXORSum(self, nums1: list[int], nums2: list[int]) -> int:
        size = len(nums1)
        dp = [10**18] * (1 << size)
        dp[0] = 0
        for mask in range(1 << size):
            used = mask.bit_count()
            for index in range(size):
                if not mask >> index & 1:
                    next_mask = mask | (1 << index)
                    dp[next_mask] = min(
                        dp[next_mask], dp[mask] + (nums1[used] ^ nums2[index])
                    )
        return dp[-1]


if __name__ == "__main__":
    test_cases = [(([1, 2], [2, 3]), 2), (([1, 0, 3], [5, 3, 4]), 8)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumXORSum(*args) == expected
