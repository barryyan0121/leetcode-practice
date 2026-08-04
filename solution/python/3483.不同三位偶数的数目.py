"""3483. 不同三位偶数的数目"""


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        numbers = set()
        for first in range(len(digits)):
            if digits[first] == 0:
                continue
            for second in range(len(digits)):
                if second == first:
                    continue
                for third in range(len(digits)):
                    if third == first or third == second or digits[third] % 2:
                        continue
                    numbers.add(
                        100 * digits[first] + 10 * digits[second] + digits[third]
                    )
        return len(numbers)


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4],), 12),
        (([0, 2, 2],), 2),
        (([6, 6, 6],), 1),
        (([1, 3, 5],), 0),
    ]
    for _, ((digits,), expected) in enumerate(test_cases):
        assert Solution().totalNumbers(digits) == expected
