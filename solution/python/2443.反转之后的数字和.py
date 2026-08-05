"""2443. 反转之后的数字和"""


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        return any(value + int(str(value)[::-1]) == num for value in range(num + 1))


if __name__ == "__main__":
    test_cases = [((443,), True), ((63,), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().sumOfNumberAndReverse(*args) == expected
