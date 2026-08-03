class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        positions = {character: index for index, character in enumerate(t)}
        return sum(
            abs(index - positions[character]) for index, character in enumerate(s)
        )


if __name__ == "__main__":
    test_cases = [("abc", "bac", 2), ("abcde", "edbac", 12)]
    for _, (s, t, expected) in enumerate(test_cases):
        assert Solution().findPermutationDifference(s, t) == expected
