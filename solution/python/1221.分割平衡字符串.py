class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = answer = 0
        for char in s:
            balance += 1 if char == "L" else -1
            if balance == 0:
                answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [("RLRRLLRLRL", 4), ("RLLLLRRRLR", 3)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().balancedStringSplit(s) == expected
