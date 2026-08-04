class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            for character in str(n):
                product *= int(character)
            if product % t == 0:
                return n
            n += 1


if __name__ == "__main__":
    test_cases = [
        ((10, 2), 10),
        ((15, 3), 16),
        ((7, 7), 7),
    ]
    for _, ((n, t), expected) in enumerate(test_cases):
        assert Solution().smallestNumber(n, t) == expected
