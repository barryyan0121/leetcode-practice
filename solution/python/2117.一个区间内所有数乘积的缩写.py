"""2117. 一个区间内所有数乘积的缩写"""

import math


class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        twos = fives = 0
        suffix = 1
        log_value = math.fsum(math.log10(value) for value in range(left, right + 1))
        for value in range(left, right + 1):
            number = value
            while number % 2 == 0:
                twos += 1
                number //= 2
            while number % 5 == 0:
                fives += 1
                number //= 5
            suffix = suffix * number % 100000
        zeros = min(twos, fives)
        suffix = (
            suffix
            * pow(2, twos - zeros, 100000)
            * pow(5, fives - zeros, 100000)
            % 100000
        )
        digits = int(log_value - zeros * math.log10(10)) + 1
        suffix_text = f"{suffix:05d}"[-5:]
        if digits <= 10:
            product = 1
            for value in range(left, right + 1):
                product *= value
            return f"{str(product).rstrip('0')}e{zeros}"
        leading = int(10 ** (log_value - int(log_value)) * 100000)
        leading_text = str(leading)[:5].zfill(5)
        return f"{leading_text}...{suffix_text}e{zeros}"


if __name__ == "__main__":
    test_cases = [((1, 4), "24e0"), ((2, 11), "399168e2")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().abbreviateProduct(*args) == expected
