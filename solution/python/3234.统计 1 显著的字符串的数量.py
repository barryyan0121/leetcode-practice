"""3234. 统计 1 显著的字符串的数量"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        zero_positions = []
        answer = 0
        for right, character in enumerate(s):
            if character == "0":
                zero_positions.append(right)
            last_zero = zero_positions[-1] if zero_positions else -1
            answer += right - last_zero
            for zeros in range(1, len(zero_positions) + 1):
                if zeros * zeros > len(s):
                    break
                last = zero_positions[-zeros]
                previous = (
                    zero_positions[-zeros - 1] if zeros < len(zero_positions) else -1
                )
                upper = min(last, right + 1 - zeros - zeros * zeros)
                if upper > previous:
                    answer += upper - previous
        return answer


if __name__ == "__main__":
    test_cases = [("00011", 5), ("101101", 16)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().numberOfSubstrings(s) == expected
