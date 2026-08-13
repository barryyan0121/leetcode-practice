class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        n = len(s)
        half = n // 2
        left = sorted(s)[:half]
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - 97] += 1
        for ch in left:
            counts[ord(ch) - 97] -= 1
        right = []
        for i in range(half):
            forbidden = ord(left[half - 1 - i]) - 97
            for x in range(26):
                if x != forbidden and counts[x]:
                    right.append(chr(x + 97))
                    counts[x] -= 1
                    break
            else:
                return "-1"
        return "".join(left + right)


if __name__ == "__main__":
    s = Solution()
    out = s.makeAntiPalindrome("aabb")
    assert out != "-1" and all(out[i] != out[-1 - i] for i in range(len(out) // 2))
    assert s.makeAntiPalindrome("aaaa") == "-1"
    print("3088 ok")
