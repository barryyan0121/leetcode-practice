"""2897. 对数组执行操作以最大化平方和"""


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        modulo = 10**9 + 7
        bits = [0] * 31
        for value in nums:
            for bit in range(31):
                bits[bit] += (value >> bit) & 1
        answer = 0
        for _ in range(k):
            value = 0
            for bit in range(31):
                if bits[bit]:
                    bits[bit] -= 1
                    value |= 1 << bit
            answer = (answer + value * value) % modulo
        return answer


if __name__ == "__main__":
    assert Solution().maxSum([2, 6, 5, 8], 2) == 261
