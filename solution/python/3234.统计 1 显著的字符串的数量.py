"""3234. 统计 1 显著的字符串的数量"""

from math import isqrt


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        max_zero = (isqrt(1 + 4 * len(s)) - 1) // 2

        for zero in range(max_zero + 1):
            last_invalid = -1
            counts = [0, 0]
            left = 0
            for right, char in enumerate(s):
                counts[ord(char) - ord("0")] += 1
                while left < right:
                    if s[left] == "0" and counts[0] > zero:
                        counts[0] -= 1
                        last_invalid = left
                        left += 1
                    elif s[left] == "1" and counts[1] - 1 >= zero * zero:
                        counts[1] -= 1
                        left += 1
                    else:
                        break
                if counts[0] == zero and counts[1] >= zero * zero:
                    answer += left - last_invalid

        return answer


if __name__ == "__main__":
    test_cases = [
        ("00011", 5),
        ("101101", 16),
    ]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().numberOfSubstrings(s) == expected
