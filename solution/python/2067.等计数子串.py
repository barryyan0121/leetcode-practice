"""2067. 等计数子串"""


class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        answer = 0
        for length in range(1, 27):
            window = length * count
            if window > len(s):
                break
            frequencies = [0] * 26
            for index, char in enumerate(s):
                frequencies[ord(char) - 97] += 1
                if index >= window:
                    frequencies[ord(s[index - window]) - 97] -= 1
                if index >= window - 1 and all(
                    value in (0, count) for value in frequencies
                ):
                    answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(("aa", 1), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().equalCountSubstrings(*args) == expected
