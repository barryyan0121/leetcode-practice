"""2531. 使字符串中不同字符的数目相等"""


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        first = [word1.count(chr(97 + i)) for i in range(26)]
        second = [word2.count(chr(97 + i)) for i in range(26)]
        for i in range(26):
            for j in range(26):
                if first[i] and second[j]:
                    a, b = first[:], second[:]
                    a[i] -= 1
                    b[j] -= 1
                    a[j] += 1
                    b[i] += 1
                    if sum(value > 0 for value in a) == sum(value > 0 for value in b):
                        return True
        return False


if __name__ == "__main__":
    test_cases = [(("a", "bb"), False), (("ab", "cd"), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isItPossible(*args) == expected
