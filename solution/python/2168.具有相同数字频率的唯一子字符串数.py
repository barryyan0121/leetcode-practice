"""2168. 具有相同数字频率的唯一子字符串数"""


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        answer = set()
        for start in range(len(s)):
            counts = [0] * 10
            for end in range(start, len(s)):
                counts[int(s[end])] += 1
                nonzero = [value for value in counts if value]
                if len(set(nonzero)) == 1:
                    answer.add(s[start : end + 1])
        return len(answer)


if __name__ == "__main__":
    test_cases = [("1212", 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().equalDigitFrequency(args) == expected
