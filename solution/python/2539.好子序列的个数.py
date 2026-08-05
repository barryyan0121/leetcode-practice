"""2539. 好子序列的个数"""


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        mod = 10**9 + 7
        counts = [s.count(chr(97 + i)) for i in range(26)]
        maximum = max(counts, default=0)
        combinations = [[0] * (maximum + 1) for _ in range(27)]
        for row in range(27):
            combinations[row][0] = 1
            for column in range(1, min(row, maximum) + 1):
                combinations[row][column] = (
                    combinations[row - 1][column - 1] + combinations[row - 1][column]
                ) % mod
        answer = 0
        for frequency in range(1, maximum + 1):
            ways = 1
            for count in counts:
                ways = ways * (combinations[count][frequency] + 1) % mod
            answer = (answer + ways - 1) % mod
        return answer


if __name__ == "__main__":
    test_cases = [(("aabb",), 11), (("abcd",), 15)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countGoodSubsequences(*args) == expected
