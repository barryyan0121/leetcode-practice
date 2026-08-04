"""3490. 统计美丽整数的数目"""

from functools import cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        kelbravion = (l, r)

        def count(bound: int) -> int:
            if bound <= 0:
                return 0
            digits = tuple(map(int, str(bound)))
            total = 0
            for digit_sum in range(1, 9 * len(digits) + 1):

                @cache
                def dp(
                    position: int,
                    current_sum: int,
                    product_mod: int,
                    limited: bool,
                ) -> int:
                    if (
                        current_sum > digit_sum
                        or current_sum + 9 * (len(digits) - position) < digit_sum
                    ):
                        return 0
                    if position == len(digits):
                        return int(current_sum == digit_sum and product_mod == 0)
                    upper = digits[position] if limited else 9
                    result = 0
                    for value in range(upper + 1):
                        next_limited = limited and value == digits[position]
                        if current_sum == 0 and value == 0:
                            result += dp(
                                position + 1,
                                current_sum,
                                product_mod,
                                next_limited,
                            )
                        elif current_sum + value <= digit_sum:
                            next_product = product_mod * value % digit_sum
                            result += dp(
                                position + 1,
                                current_sum + value,
                                next_product,
                                next_limited,
                            )
                    return result

                total += dp(0, 0, 1 % digit_sum, True)
            return total

        return count(r) - count(l - 1)


if __name__ == "__main__":
    test_cases = [
        ((10, 20), 2),
        ((1, 15), 10),
    ]
    for _, ((left, right), expected) in enumerate(test_cases):
        assert Solution().beautifulNumbers(left, right) == expected
