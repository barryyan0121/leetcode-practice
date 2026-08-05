"""3792. 递增乘积块之和"""


class Solution:
    def sumOfBlocks(self, n: int) -> int:
        mod = 10**9 + 7
        answer = 0
        start = 1
        for length in range(1, n + 1):
            current = 1
            for value in range(start, start + length):
                current = current * value % mod
            answer = (answer + current) % mod
            start += length
        return answer


if __name__ == "__main__":
    test_cases = [((3,), 127), ((7,), 6997165)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().sumOfBlocks(*args) == expected
