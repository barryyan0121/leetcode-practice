class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        modulo = 10**9 + 7
        length = len(s)
        combinations = [[0] * (length + 1) for _ in range(length + 1)]
        for row in range(length + 1):
            combinations[row][0] = combinations[row][row] = 1
            for column in range(1, row):
                combinations[row][column] = (
                    combinations[row - 1][column - 1] + combinations[row - 1][column]
                ) % modulo

        valid = [False] * (length + 1)
        for ones in range(1, length + 1):
            steps = 0
            value = ones
            while value != 1:
                value = value.bit_count()
                steps += 1
            valid[ones] = steps + 1 <= k

        answer = 0
        used = 0
        for index, bit in enumerate(s):
            if bit == "1":
                remaining = length - index - 1
                for ones in range(1, remaining + 2):
                    if valid[used + ones - 1]:
                        answer = (answer + combinations[remaining][ones - 1]) % modulo
                used += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (("111", 1), 3),
        (("1000", 2), 6),
        (("10", 1), 1),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().countKReducibleNumbers(s, k) == expected
