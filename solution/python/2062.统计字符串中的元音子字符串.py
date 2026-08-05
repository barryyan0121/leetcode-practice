"""2062. 统计字符串中的元音子字符串"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        answer = left = 0
        for right, char in enumerate(word):
            if char not in vowels:
                left = right + 1
            seen = set()
            for index in range(right, left - 1, -1):
                seen.add(word[index])
                if len(seen) == 5:
                    answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [("aeiouu", 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countVowelSubstrings(args) == expected
