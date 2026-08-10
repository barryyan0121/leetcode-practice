"""3068. 节点值的最大和"""


class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        even, odd = 0, -(10**18)
        for value in nums:
            even, odd = max(even + value, odd + (value ^ k)), max(
                odd + value, even + (value ^ k)
            )
        return even


if __name__ == "__main__":
    assert Solution().maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]) == 6
