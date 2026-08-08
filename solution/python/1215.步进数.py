from typing import List


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        result = [0] if low == 0 else []

        def dfs(number: int) -> None:
            if number > high:
                return
            if number >= low:
                result.append(number)
            digit = number % 10
            for next_digit in (digit - 1, digit + 1):
                if 0 <= next_digit <= 9:
                    dfs(number * 10 + next_digit)

        for number in range(1, 10):
            dfs(number)
        return sorted(result)


if __name__ == "__main__":
    test_cases = [(0, 21, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21])]
    for _, (low, high, expected) in enumerate(test_cases):
        assert Solution().countSteppingNumbers(low, high) == expected
