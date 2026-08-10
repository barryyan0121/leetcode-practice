from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ca, cb = Counter(a), Counter(b)
        pa = [0] * 27
        pb = [0] * 27
        for i in range(26):
            pa[i + 1] = pa[i] + ca[chr(97 + i)]
            pb[i + 1] = pb[i] + cb[chr(97 + i)]
        result = len(a) + len(b) - max((ca | cb).values())
        for split in range(1, 26):
            result = min(result, pa[split] + len(b) - pb[split])
            result = min(result, pb[split] + len(a) - pa[split])
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.minCharacters("aba", "caa") == 2
    assert solution.minCharacters("dabadd", "cda") == 3
    assert solution.minCharacters("a", "b") == 0
    print("1737 passed")
