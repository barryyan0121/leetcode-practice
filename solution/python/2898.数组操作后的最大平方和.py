"""2898. 数组操作后的最大平方和"""


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        counts = [0] * 31
        for number in nums:
            for bit in range(31):
                counts[bit] += number >> bit & 1
        answer = 0
        for _ in range(k):
            value = 0
            for bit in range(31):
                if counts[bit]:
                    value |= 1 << bit
                    counts[bit] -= 1
            answer += value * value
        return answer


if __name__ == "__main__":
    assert Solution().maxSum([1], 1) == 1
