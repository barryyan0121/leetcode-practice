"""2030. 含特定字母的最小子序列"""


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        remaining = s.count(letter)
        chosen = 0
        stack = []
        for i, char in enumerate(s):
            if char == letter:
                remaining -= 1
            while stack and stack[-1] > char and len(stack) - 1 + len(s) - i >= k:
                if (
                    stack[-1] == letter
                    and chosen - 1 + remaining + (char == letter) < repetition
                ):
                    break
                chosen -= stack.pop() == letter
            if len(stack) < k:
                if char == letter or k - len(stack) > repetition - chosen:
                    stack.append(char)
                    chosen += char == letter
        return "".join(stack)


if __name__ == "__main__":
    test_cases = [(("leet", 3, "e", 1), "eet")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().smallestSubsequence(*args) == expected
