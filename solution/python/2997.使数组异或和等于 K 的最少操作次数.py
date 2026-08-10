"""2997. 使数组异或和等于 K 的最少操作次数"""


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        value = k
        for number in nums:
            value ^= number
        return value.bit_count()


if __name__ == "__main__":
    assert Solution().minOperations([2, 1, 3, 4], 1) == 2
