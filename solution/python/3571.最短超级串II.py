"""3571. 最短超级串 II"""


class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        if s1 in s2:
            return s2
        if s2 in s1:
            return s1

        def merge(left, right):
            overlap = 0
            for size in range(1, min(len(left), len(right)) + 1):
                if left[-size:] == right[:size]:
                    overlap = size
            return left + right[overlap:]

        first, second = merge(s1, s2), merge(s2, s1)
        return first if len(first) <= len(second) else second


if __name__ == "__main__":
    test_cases = [
        (("aba", "bab"), "abab"),
        (("aa", "aaa"), "aaa"),
    ]
    for _, ((s1, s2), expected) in enumerate(test_cases):
        assert Solution().shortestSuperstring(s1, s2) == expected
