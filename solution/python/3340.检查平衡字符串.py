class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(map(int, num[::2])) == sum(map(int, num[1::2]))


if __name__ == "__main__":
    test_cases = [
        (("1234",), False),
        (("24123",), True),
        (("1221",), True),
    ]
    for _, ((num,), expected) in enumerate(test_cases):
        assert Solution().isBalanced(num) == expected
