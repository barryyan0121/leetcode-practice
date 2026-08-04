class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        rounds = min(x, y // 4)
        return "Alice" if rounds % 2 else "Bob"


if __name__ == "__main__":
    test_cases = [((2, 7), "Alice"), ((4, 11), "Bob")]
    for _, ((x, y), expected) in enumerate(test_cases):
        assert Solution().winningPlayer(x, y) == expected
