class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")

        def at_most(limit: int) -> int:
            if limit < 0:
                return 0
            last_seen = {vowel: -1 for vowel in vowels}
            left = consonants = result = 0
            for right, character in enumerate(word):
                if character in vowels:
                    last_seen[character] = right
                else:
                    consonants += 1
                while consonants > limit:
                    if word[left] not in vowels:
                        consonants -= 1
                    left += 1
                first_vowel = min(last_seen.values())
                if first_vowel >= left:
                    result += first_vowel - left + 1
            return result

        return at_most(k) - at_most(k - 1)


if __name__ == "__main__":
    test_cases = [
        (("aeioqq", 1), 0),
        (("aeiou", 0), 1),
        (("ieaouqqieaouqq", 1), 3),
    ]
    for _, ((word, k), expected) in enumerate(test_cases):
        assert Solution().countOfSubstrings(word, k) == expected
