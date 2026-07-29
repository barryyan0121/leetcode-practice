class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        modulo = 10**9 + 7
        size = min(arrLen, steps // 2 + 1)
        ways = [1] + [0] * (size - 1)
        for _ in range(steps):
            padded = [0] + ways + [0]
            ways = [sum(padded[index : index + 3]) % modulo for index in range(size)]
        return ways[0]


if __name__ == "__main__":
    test_cases = [((3, 2), 4), ((2, 4), 2), ((4, 2), 8)]
    for _, ((steps, arr_len), expected) in enumerate(test_cases):
        assert Solution().numWays(steps, arr_len) == expected
