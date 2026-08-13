class Solution:
    def findNumber(self) -> int:
        ans = 0
        for i in range(30):
            if commonSetBits(1 << i) > 0:
                ans |= 1 << i
        return ans


if __name__ == "__main__":
    hidden = 42

    def commonSetBits(num: int) -> int:
        return (hidden & num).bit_count()

    test_cases = [(Solution().findNumber(), hidden)]
    for _, (actual, expected) in enumerate(test_cases):
        assert actual == expected
