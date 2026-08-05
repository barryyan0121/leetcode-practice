"""2038. 如果相邻两个颜色均相同则删除当前颜色"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = bob = 0
        for index in range(1, len(colors) - 1):
            if colors[index - 1] == colors[index] == colors[index + 1]:
                if colors[index] == "A":
                    alice += 1
                else:
                    bob += 1
        return alice > bob


if __name__ == "__main__":
    test_cases = [("AAABABB", True), ("AA", False)]
    for _, (colors, expected) in enumerate(test_cases):
        assert Solution().winnerOfGame(colors) == expected
