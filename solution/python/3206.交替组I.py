class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        n = len(colors)
        return sum(
            colors[(index - 1) % n] != colors[index]
            and colors[index] != colors[(index + 1) % n]
            for index in range(n)
        )


if __name__ == "__main__":
    test_cases = [([1, 1, 1], 0), ([0, 1, 0, 0, 1], 3)]
    for _, (colors, expected) in enumerate(test_cases):
        assert Solution().numberOfAlternatingGroups(colors) == expected
