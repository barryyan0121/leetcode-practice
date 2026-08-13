"""3233. 非特殊数字的数目"""


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def prime(number: int) -> bool:
            if number < 2:
                return False
            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    return False
                divisor += 1
            return True

        special = sum(
            prime(root) for root in range(2, int(r**0.5) + 1) if l <= root * root <= r
        )
        return r - l + 1 - special


if __name__ == "__main__":
    test_cases = [
        ((5, 10), 5),
        ((1, 4), 3),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().nonSpecialCount(*args) == expected, index
