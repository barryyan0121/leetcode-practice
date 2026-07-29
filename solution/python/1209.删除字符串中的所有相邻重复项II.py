class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return "".join(char * count for char, count in stack)


if __name__ == "__main__":
    test_cases = [("deeedbbcccbdaa", 3, "aa"), ("pbbcggttciiippooaais", 2, "ps")]
    for _, (s, k, expected) in enumerate(test_cases):
        assert Solution().removeDuplicates(s, k) == expected
