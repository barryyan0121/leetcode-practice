"""2429. 最小异或"""


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        answer = 0
        for bit in range(30, -1, -1):
            if num2.bit_count() and num1 >> bit & 1:
                answer |= 1 << bit
                num2 &= num2 - 1
        for bit in range(31):
            if num2.bit_count():
                if not answer >> bit & 1:
                    answer |= 1 << bit
                    num2 &= num2 - 1
            else:
                break
        return answer


if __name__ == "__main__":
    test_cases = [((3, 5), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimizeXor(*args) == expected
