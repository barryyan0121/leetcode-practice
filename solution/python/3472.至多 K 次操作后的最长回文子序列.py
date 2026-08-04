class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        draxemilon = (s, k)
        size = len(s)

        def change_cost(left, right):
            difference = abs(ord(s[left]) - ord(s[right]))
            return min(difference, 26 - difference)

        previous = [[1] * (k + 1) for _ in range(size)]
        if size == 1:
            return 1
        inner = [[1] * (k + 1) for _ in range(size - 1)]
        for left in range(size - 1):
            cost = change_cost(left, left + 1)
            values = [1] * (k + 1)
            for budget in range(cost, k + 1):
                values[budget] = 2
            previous[left] = values
        for length in range(3, size + 1):
            current = []
            for left in range(size - length + 1):
                right = left + length - 1
                left_skip = previous[left]
                right_skip = previous[left + 1]
                inside = inner[left + 1]
                cost = change_cost(left, right)
                values = [0] * (k + 1)
                for budget in range(k + 1):
                    best = max(left_skip[budget], right_skip[budget])
                    if budget >= cost:
                        best = max(best, 2 + inside[budget - cost])
                    values[budget] = best
                current.append(values)
            inner, previous = previous, current
        return previous[0][k]


if __name__ == "__main__":
    test_cases = [
        (("abced", 2), 3),
        (("aaazzz", 4), 6),
        (("a", 1), 1),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().longestPalindromicSubsequence(s, k) == expected
