"""2484. 统计回文子序列数目"""


class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 10**9 + 7
        digits = [int(char) for char in s]
        n = len(digits)
        left_digits = [0] * 10
        right_digits = [0] * 10
        left_pairs = [[0] * 10 for _ in range(10)]
        right_pairs = [[0] * 10 for _ in range(10)]
        for value in digits[1:]:
            for first in range(10):
                right_pairs[first][value] += right_digits[first]
            right_digits[value] += 1
        answer = 0
        for center in range(n):
            if 2 <= center <= n - 3:
                for first in range(10):
                    for second in range(10):
                        answer += left_pairs[first][second] * right_pairs[second][first]
                answer %= mod
            if center + 1 < n:
                value = digits[center + 1]
                for last in range(10):
                    right_pairs[value][last] -= right_digits[last] - (last == value)
                right_digits[value] -= 1
            value = digits[center]
            for first in range(10):
                left_pairs[first][value] += left_digits[first]
            left_digits[value] += 1
        return answer


if __name__ == "__main__":
    assert Solution().countPalindromes("103301") == 2
