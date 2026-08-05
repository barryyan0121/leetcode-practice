"""2595. 奇偶位数"""


class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        answer = [0, 0]
        index = 0
        while n:
            answer[index] += n & 1
            n >>= 1
            index ^= 1
        return answer


if __name__ == "__main__":
    test_cases = [((17,), [2, 0])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().evenOddBit(*args) == expected
