class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        answer = 0
        for length, char in enumerate(s, 1):
            seen.add(char)
            if len(seen) == length % 3:
                answer += 1
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.residuePrefixes("abc") == 2
    assert s.residuePrefixes("dd") == 1
    assert s.residuePrefixes("bob") == 2
