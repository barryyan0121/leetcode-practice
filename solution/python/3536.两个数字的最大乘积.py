class Solution:
    def maxProduct(self, n: int) -> int:
        largest = second = 0
        while n:
            digit = n % 10
            if digit >= largest:
                largest, second = digit, largest
            elif digit > second:
                second = digit
            n //= 10
        return largest * second


if __name__ == "__main__":
    test_cases = [
        (31, 3),
        (22, 4),
        (124, 8),
    ]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().maxProduct(n) == expected
