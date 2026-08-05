"""2167. 移除包含非法货物的最少时间"""


class Solution:
    def minimumTime(self, s: str) -> int:
        best_prefix = 0
        answer = len(s)
        for index, char in enumerate(s):
            best_prefix = min(best_prefix + (2 if char == "1" else 0), index + 1)
            answer = min(answer, best_prefix + len(s) - index - 1)
        return answer


if __name__ == "__main__":
    test_cases = [(("1100101",), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumTime(*args) == expected
