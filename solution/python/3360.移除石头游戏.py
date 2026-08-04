class Solution:
    def canAliceWin(self, n: int) -> bool:
        moves = 0
        remaining = n
        stones = 10
        while remaining >= stones:
            remaining -= stones
            moves += 1
            stones -= 1
        return moves % 2 == 1


if __name__ == "__main__":
    test_cases = [
        ((12,), True),
        ((1,), False),
        ((19,), False),
        ((20,), False),
    ]
    for _, ((n,), expected) in enumerate(test_cases):
        assert Solution().canAliceWin(n) == expected
