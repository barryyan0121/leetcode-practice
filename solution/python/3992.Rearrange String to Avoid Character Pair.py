"""3992. Rearrange String to Avoid Character Pair"""


class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        chars = list(s)
        next_y = 0
        for index, char in enumerate(chars):
            if char == y:
                chars[next_y], chars[index] = chars[index], chars[next_y]
                next_y += 1
        return "".join(chars)


if __name__ == "__main__":
    test_cases = [
        (("aabc", "a", "c"), "cbaa"),
        (("dcab", "d", "b"), "bacd"),
        (("axe", "o", "x"), "xae"),
    ]
    for _, (args, _) in enumerate(test_cases):
        result = Solution().rearrangeString(*args)
        s, x, y = args
        assert sorted(result) == sorted(s)
        assert max(
            (index for index, char in enumerate(result) if char == y), default=-1
        ) < min(
            (index for index, char in enumerate(result) if char == x),
            default=len(result),
        )
