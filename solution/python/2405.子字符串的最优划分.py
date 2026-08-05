"""2405. 子字符串的最优划分"""


class Solution:
    def partitionString(self, s: str) -> int:
        answer, seen = 1, set()
        for char in s:
            if char in seen:
                answer += 1
                seen.clear()
            seen.add(char)
        return answer


if __name__ == "__main__":
    test_cases = [(("abacaba",), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().partitionString(*args) == expected
