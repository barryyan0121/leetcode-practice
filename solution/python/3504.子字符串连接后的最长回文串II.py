class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def palindrome_lengths(word: str, starts: bool) -> list[int]:
            lengths = [0] * len(word)
            for center in range(len(word)):
                left = right = center
                while left >= 0 and right < len(word) and word[left] == word[right]:
                    length = right - left + 1
                    index = left if starts else right
                    lengths[index] = max(lengths[index], length)
                    left -= 1
                    right += 1
                left, right = center, center + 1
                while left >= 0 and right < len(word) and word[left] == word[right]:
                    length = right - left + 1
                    index = left if starts else right
                    lengths[index] = max(lengths[index], length)
                    left -= 1
                    right += 1
            return lengths

        starts = palindrome_lengths(s, True)
        ends = palindrome_lengths(t, False)
        answer = max(max(starts), max(ends))
        previous = [0] * len(t)
        for i in range(len(s) - 1, -1, -1):
            current = [0] * len(t)
            for j, value in enumerate(t):
                current[j] = max(starts[i], ends[j])
                if s[i] == value:
                    if i + 1 < len(s) and j:
                        inner = previous[j - 1]
                    elif i + 1 < len(s):
                        inner = starts[i + 1]
                    elif j:
                        inner = ends[j - 1]
                    else:
                        inner = 0
                    current[j] = max(current[j], 2 + inner)
                answer = max(answer, current[j])
            previous = current
        return answer


if __name__ == "__main__":
    test_cases = [
        (("a", "a"), 2),
        (("abc", "def"), 1),
        (("b", "aaaa"), 4),
        (("abcde", "ecdba"), 5),
        (("mrb", "r"), 3),
    ]
    for _, ((s, t), expected) in enumerate(test_cases):
        assert Solution().longestPalindrome(s, t) == expected
