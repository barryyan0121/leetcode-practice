class Solution:
    def getSmallestString(self, s: str) -> str:
        chars = list(s)
        for index in range(len(chars) - 1):
            if (
                chars[index] > chars[index + 1]
                and int(chars[index]) % 2 == int(chars[index + 1]) % 2
            ):
                chars[index], chars[index + 1] = chars[index + 1], chars[index]
                break
        return "".join(chars)


if __name__ == "__main__":
    test_cases = [("45320", "43520"), ("001", "001")]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().getSmallestString(s) == expected
