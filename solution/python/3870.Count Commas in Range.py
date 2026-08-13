class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        base = 1
        while base * 1000 <= n:
            base *= 1000
            count += 1

        result = 0
        base = 1
        for _ in range(count):
            base *= 1000
            result += n - base + 1
        return result


if __name__ == "__main__":
    test_cases = [
        (1002, 3),
        (998, 0),
    ]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().countCommas(n) == expected
