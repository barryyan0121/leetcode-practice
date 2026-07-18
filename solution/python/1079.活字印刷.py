from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles)

        def dfs() -> int:
            total = 0
            for tile in counts:
                if counts[tile]:
                    counts[tile] -= 1
                    total += 1 + dfs()
                    counts[tile] += 1
            return total

        return dfs()


if __name__ == "__main__":
    test_cases = [("AAB", 8), ("V", 1), ("AAABBC", 188)]
    for _, (tiles, expected) in enumerate(test_cases):
        assert Solution().numTilePossibilities(tiles) == expected
