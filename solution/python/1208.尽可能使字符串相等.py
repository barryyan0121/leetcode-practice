class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = answer = 0
        for right, (source, target) in enumerate(zip(s, t)):
            cost += abs(ord(source) - ord(target))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    test_cases = [("abcd", "bcdf", 3, 3), ("abcd", "cdef", 3, 1)]
    for _, (s, t, max_cost, expected) in enumerate(test_cases):
        assert Solution().equalSubstring(s, t, max_cost) == expected
