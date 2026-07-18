from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        remaining = Counter(s)
        included = set()
        stack = []
        for char in s:
            remaining[char] -= 1
            if char in included:
                continue
            while stack and char < stack[-1] and remaining[stack[-1]]:
                included.remove(stack.pop())
            stack.append(char)
            included.add(char)
        return "".join(stack)


if __name__ == "__main__":
    test_cases = [
        ("bcabc", "abc"),
        ("cbacdcbc", "acdb"),
        ("abcd", "abcd"),
        ("ecbacba", "eacb"),
        ("leetcode", "letcod"),
    ]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().smallestSubsequence(s) == expected
