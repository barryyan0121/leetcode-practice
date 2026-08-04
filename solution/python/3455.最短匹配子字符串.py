from bisect import bisect_left


class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        xaldrovine = (s, p)
        first, second, third = p.split("*")

        def starts(word):
            if not word:
                return list(range(len(s) + 1))
            pi = [0] * len(word)
            for i in range(1, len(word)):
                j = pi[i - 1]
                while j and word[i] != word[j]:
                    j = pi[j - 1]
                pi[i] = j + (word[i] == word[j])
            result = []
            j = 0
            for i, char in enumerate(s):
                while j and char != word[j]:
                    j = pi[j - 1]
                j += char == word[j]
                if j == len(word):
                    result.append(i - len(word) + 1)
                    j = pi[j - 1]
            return result

        first_starts, second_starts, third_starts = map(starts, (first, second, third))
        answer = len(s) + 1
        for start in first_starts:
            second_index = bisect_left(second_starts, start + len(first))
            if second_index == len(second_starts):
                continue
            middle = second_starts[second_index]
            third_index = bisect_left(third_starts, middle + len(second))
            if third_index < len(third_starts):
                answer = min(answer, third_starts[third_index] + len(third) - start)
        return -1 if answer == len(s) + 1 else answer


if __name__ == "__main__":
    test_cases = [
        (("abaacbaecebce", "ba*c*ce"), 8),
        (("baccbaadbc", "cc*baa*adb"), -1),
        (("a", "**"), 0),
        (("madlogic", "*adlogi*"), 6),
    ]
    for _, ((s, p), expected) in enumerate(test_cases):
        assert Solution().shortestMatchingSubstring(s, p) == expected
