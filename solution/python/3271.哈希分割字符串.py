class Solution:
    def stringHash(self, s: str, k: int) -> str:
        return "".join(
            chr(
                sum(ord(character) - ord("a") for character in s[start : start + k])
                % 26
                + ord("a")
            )
            for start in range(0, len(s), k)
        )


if __name__ == "__main__":
    test_cases = [(("abcd", 2), "bf"), (("mxz", 3), "i")]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().stringHash(s, k) == expected
