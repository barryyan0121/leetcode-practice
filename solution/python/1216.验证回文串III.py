class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        previous = [0] * (len(s) + 1)
        for char in s:
            current = [0]
            for index, other in enumerate(reversed(s), 1):
                current.append(
                    previous[index - 1] + 1
                    if char == other
                    else max(previous[index], current[-1])
                )
            previous = current
        return len(s) - previous[-1] <= k


if __name__ == "__main__":
    test_cases = [("abcdeca", 2, True), ("abbababa", 1, True)]
    for _, (s, k, expected) in enumerate(test_cases):
        assert Solution().isValidPalindrome(s, k) == expected
