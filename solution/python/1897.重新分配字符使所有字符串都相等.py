"""1897. 重新分配字符使所有字符串都相等"""


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        counts = [0] * 26
        for word in words:
            for char in word:
                counts[ord(char) - 97] += 1
        return all(count % len(words) == 0 for count in counts)


if __name__ == "__main__":
    test_cases = [(["abc", "aabc", "bc"], True), (["ab", "a"], False)]
    for _, (words, expected) in enumerate(test_cases):
        assert Solution().makeEqual(words) == expected
