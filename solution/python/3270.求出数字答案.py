"""3270. 求出数字答案"""


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        digits1 = str(num1).zfill(4)
        digits2 = str(num2).zfill(4)
        digits3 = str(num3).zfill(4)
        key = "".join(
            str(min(int(a), int(b), int(c)))
            for a, b, c in zip(digits1, digits2, digits3)
        )
        return int(key)


if __name__ == "__main__":
    test_cases = [
        ((1, 10, 1000), 0),
        ((987, 879, 798), 777),
        ((1, 2, 3), 1),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().generateKey(*args) == expected
