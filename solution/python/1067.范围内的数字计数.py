class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count(number: int) -> int:
            answer = 0
            factor = 1
            while factor <= number:
                lower = number % factor
                current = number // factor % 10
                higher = number // (factor * 10)
                if d:
                    answer += higher * factor
                    if current > d:
                        answer += factor
                    elif current == d:
                        answer += lower + 1
                elif higher:
                    answer += (higher - 1) * factor + (
                        lower + 1 if current == 0 else factor
                    )
                factor *= 10
            return answer

        return count(high) - count(low - 1)


if __name__ == "__main__":
    test_cases = [(1, 1, 13, 6), (3, 100, 250, 35), (0, 1, 10, 1)]
    for _, (digit, low, high, expected) in enumerate(test_cases):
        assert Solution().digitsCount(digit, low, high) == expected
