class Solution:
    def confusingNumberII(self, n: int) -> int:
        rotated_digits = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        count = 0

        def dfs(value: int, rotated: int, base: int) -> None:
            nonlocal count
            if value != rotated:
                count += 1
            for digit, rotated_digit in rotated_digits.items():
                next_value = value * 10 + digit
                if next_value <= n:
                    dfs(next_value, rotated_digit * base + rotated, base * 10)

        for digit in (1, 6, 8, 9):
            if digit <= n:
                dfs(digit, rotated_digits[digit], 10)
        return count


if __name__ == "__main__":
    test_cases = [(1, 0), (6, 1), (20, 6), (100, 19)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().confusingNumberII(n) == expected
