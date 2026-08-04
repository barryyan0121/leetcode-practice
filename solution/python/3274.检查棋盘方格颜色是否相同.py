class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return (ord(coordinate1[0]) + int(coordinate1[1])) % 2 == (
            ord(coordinate2[0]) + int(coordinate2[1])
        ) % 2


if __name__ == "__main__":
    test_cases = [(("a1", "c3"), True), (("a1", "h3"), False)]
    for _, ((coordinate1, coordinate2), expected) in enumerate(test_cases):
        assert Solution().checkTwoChessboards(coordinate1, coordinate2) == expected
