class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        answer = 0
        for left in range(len(s)):
            count_vowels = count_consonants = 0
            for right in range(left, len(s)):
                if s[right] in vowels:
                    count_vowels += 1
                else:
                    count_consonants += 1
                if (
                    count_vowels == count_consonants
                    and count_vowels * count_consonants % k == 0
                ):
                    answer += 1
        return answer


assert Solution().beautifulSubstrings("baeyh", 2) == 2
