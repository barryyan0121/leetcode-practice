class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = list(s)
        for index in range(1, len(chars), 2):
            chars[index] = chr(ord(chars[index - 1]) + int(chars[index]))
        return "".join(chars)


if __name__ == "__main__":
    solution = Solution()
    assert solution.replaceDigits("a1c1e1") == "abcdef"
    print("1844 passed")
