class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        target = self._factor(t)
        if target is None:
            return "-1"

        n = len(num)
        factors = [self._factor(int(d)) for d in "123456789"]
        infinity = sum(target) + 1
        memo = {}

        def minimum_digits(need):
            if max(need) == 0:
                return 0
            if need in memo:
                return memo[need]
            best = infinity
            for digit_factor in factors:
                next_need = tuple(
                    max(0, need[index] - digit_factor[index]) for index in range(4)
                )
                if next_need != need:
                    best = min(best, 1 + minimum_digits(next_need))
            memo[need] = best
            return best

        def subtract(need, digit):
            digit_factor = factors[digit - 1]
            return tuple(
                max(0, need[index] - digit_factor[index]) for index in range(4)
            )

        def build(length, need):
            if minimum_digits(need) > length:
                return None
            result = []
            for position in range(length):
                remaining = length - position - 1
                for digit in range(1, 10):
                    next_need = subtract(need, digit)
                    if minimum_digits(next_need) <= remaining:
                        result.append(str(digit))
                        need = next_need
                        break
            return "".join(result)

        prefix = [(0, 0, 0, 0)]
        valid_prefix = [True]
        for character in num:
            digit_factor = (
                (0, 0, 0, 0) if character == "0" else self._factor(int(character))
            )
            prefix.append(
                tuple(
                    min(target[index], prefix[-1][index] + digit_factor[index])
                    for index in range(4)
                )
            )
            valid_prefix.append(valid_prefix[-1] and character != "0")

        if valid_prefix[-1] and prefix[-1] == target:
            return num

        for position in range(n - 1, -1, -1):
            if not valid_prefix[position]:
                continue
            for digit in range(int(num[position]) + 1, 10):
                need = tuple(
                    max(
                        0,
                        target[index]
                        - prefix[position][index]
                        - factors[digit - 1][index],
                    )
                    for index in range(4)
                )
                suffix = build(n - position - 1, need)
                if suffix is not None:
                    return num[:position] + str(digit) + suffix

        return build(max(n + 1, minimum_digits(target)), target) or "-1"

    @staticmethod
    def _factor(value):
        result = []
        for prime in (2, 3, 5, 7):
            count = 0
            while value % prime == 0:
                value //= prime
                count += 1
            result.append(count)
        return tuple(result) if value == 1 else None


if __name__ == "__main__":
    test_cases = [
        (("1234", 256), "1488"),
        (("12355", 50), "12355"),
        (("11111", 26), "-1"),
        (("10", 2), "12"),
        (("19", 2), "21"),
        (("111", 7), "117"),
        (("999", 7), "1117"),
        (("12", 1968750), "255555579"),
    ]
    for _, ((num, t), expected) in enumerate(test_cases):
        assert Solution().smallestNumber(num, t) == expected
