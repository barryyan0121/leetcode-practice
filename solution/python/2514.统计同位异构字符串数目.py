"""2514. 统计同位异构字符串数目"""

from math import factorial


class Solution:
    def countAnagrams(self, s: str) -> int:
        mod = 10**9 + 7
        answer = 1
        for word in s.split():
            ways = factorial(len(word))
            for char in set(word):
                ways //= factorial(word.count(char))
            answer = answer * ways % mod
        return answer


if __name__ == "__main__":
    test_cases = [(("too hot",), 18)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countAnagrams(*args) == expected
