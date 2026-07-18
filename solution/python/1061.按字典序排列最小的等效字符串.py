class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in zip(s1, s2):
            a, b = find(ord(a) - 97), find(ord(b) - 97)
            parent[max(a, b)] = min(a, b)
        return "".join(chr(find(ord(c) - 97) + 97) for c in baseStr)


if __name__ == "__main__":
    test_cases = [("parker", "morris", "parser", "makkek")]
    for _, (s1, s2, base, expected) in enumerate(test_cases):
        assert Solution().smallestEquivalentString(s1, s2, base) == expected
