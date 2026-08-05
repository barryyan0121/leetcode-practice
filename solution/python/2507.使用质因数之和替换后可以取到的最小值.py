"""2507. 使用质因数之和替换后可以取到的最小值"""


class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            original = n
            factor, total = 2, 0
            while factor * factor <= n:
                while n % factor == 0:
                    total += factor
                    n //= factor
                factor += 1
            if n > 1:
                total += n
            if total == original:
                return n if total == 0 else total
            n = total


if __name__ == "__main__":
    test_cases = [((15,), 5), ((4,), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().smallestValue(*args) == expected
