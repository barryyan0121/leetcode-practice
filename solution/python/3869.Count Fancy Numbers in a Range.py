class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def digit_count(value: int) -> int:
            if value <= 0:
                return 0
            count = 0
            while value:
                value //= 10
                count += 1
            return count

        def digit_sum(value: int) -> int:
            total = 0
            while value:
                value, remainder = divmod(value, 10)
                total += remainder
            return total

        def is_good(value: int) -> bool:
            if value < 10:
                return True
            digits = []
            while value:
                digits.append(value % 10)
                value //= 10
            digits.reverse()
            increasing = all(a < b for a, b in zip(digits, digits[1:]))
            decreasing = all(a > b for a, b in zip(digits, digits[1:]))
            return increasing or decreasing

        def build_good(bound: int) -> list[int]:
            result = [value for value in range(1, min(9, bound) + 1)]
            for step in (1, -1):
                queue = result[:]
                while queue:
                    next_queue = []
                    for value in queue:
                        digit = value % 10 + step
                        while 0 <= digit <= 9:
                            new_value = value * 10 + digit
                            if new_value <= bound:
                                result.append(new_value)
                                next_queue.append(new_value)
                            digit += step
                    queue = next_queue
            return result

        def count_up_to(bound: int) -> int:
            if bound <= 0:
                return 0
            sum_is_good = [is_good(value) for value in range(digit_count(bound) * 9 + 1)]
            good_numbers = build_good(bound)
            total = 0
            for value in range(1, bound + 1):
                if is_good(value) or sum_is_good[digit_sum(value)]:
                    total += 1
            return total

        return count_up_to(r) - count_up_to(l - 1)


if __name__ == "__main__":
    test_cases = [
        ((8, 10), 3),
        ((12340, 12341), 1),
    ]
    for _, ((left, right), expected) in enumerate(test_cases):
        assert Solution().countFancy(left, right) == expected
