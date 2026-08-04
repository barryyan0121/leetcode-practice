class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]
    ) -> int:
        cuts = [(cost, 0) for cost in horizontalCut] + [
            (cost, 1) for cost in verticalCut
        ]
        horizontal_pieces = vertical_pieces = 1
        total = 0
        for cost, direction in sorted(cuts, reverse=True):
            if direction == 0:
                total += cost * vertical_pieces
                horizontal_pieces += 1
            else:
                total += cost * horizontal_pieces
                vertical_pieces += 1
        return total


if __name__ == "__main__":
    test_cases = [
        ((3, 2, [1, 3], [5]), 13),
        ((2, 2, [7], [4]), 15),
    ]
    for _, ((m, n, horizontal, vertical), expected) in enumerate(test_cases):
        assert Solution().minimumCost(m, n, horizontal, vertical) == expected
