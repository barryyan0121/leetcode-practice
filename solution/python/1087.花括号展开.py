class Solution:
    def expand(self, s: str) -> list[str]:
        choices = []
        index = 0
        while index < len(s):
            if s[index] == "{":
                end = s.index("}", index)
                choices.append(s[index + 1 : end].split(","))
                index = end + 1
            else:
                choices.append([s[index]])
                index += 1
        words = [""]
        for chars in choices:
            words = [word + char for word in words for char in chars]
        return sorted(words)


if __name__ == "__main__":
    test_cases = [
        ("{a,b}c{d,e}f", ["acdf", "acef", "bcdf", "bcef"]),
        ("abcd", ["abcd"]),
        ("{a,b}{z,y,x}", ["ax", "ay", "az", "bx", "by", "bz"]),
    ]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().expand(s) == expected
