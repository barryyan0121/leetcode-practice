"""3853. 合并靠近字符"""


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        chars = list(s)
        while True:
            merged = False
            for left in range(len(chars)):
                for right in range(left + 1, min(len(chars), left + k + 1)):
                    if chars[left] == chars[right]:
                        chars.pop(right)
                        merged = True
                        break
                if merged:
                    break
            if not merged:
                return "".join(chars)


if __name__ == "__main__":
    test_cases = [
        (("abca", 3), "abc"),
        (("aabca", 2), "abca"),
        (("yybyzybz", 2), "ybzybz"),
    ]
    for args, expected in test_cases:
        assert Solution().mergeCharacters(*args) == expected
