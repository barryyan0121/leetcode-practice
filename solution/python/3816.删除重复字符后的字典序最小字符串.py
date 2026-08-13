from bisect import bisect_left


class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        n = len(s)
        positions = [[] for _ in range(26)]
        for i, char in enumerate(s):
            positions[ord(char) - 97].append(i)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | 1 << (ord(s[i]) - 97)
        missing = suffix[0]
        answer = []
        start = 0
        while missing:
            for c in range(26):
                occurrences = positions[c]
                j = bisect_left(occurrences, start)
                if j < len(occurrences) and suffix[occurrences[j]] & missing == missing:
                    answer.append(chr(c + 97))
                    start = occurrences[j] + 1
                    missing &= ~(1 << c)
                    break
        return "".join(answer)


if __name__ == "__main__":
    solution = Solution()
    assert solution.lexSmallestAfterDeletion("aaccb") == "aacb"
    assert solution.lexSmallestAfterDeletion("z") == "z"
