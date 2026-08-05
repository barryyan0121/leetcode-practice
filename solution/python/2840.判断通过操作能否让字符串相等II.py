class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return all(sorted(s1[i::2]) == sorted(s2[i::2]) for i in (0, 1))


if __name__ == "__main__":
    assert Solution().checkStrings("abcdba", "cabdab") is True
