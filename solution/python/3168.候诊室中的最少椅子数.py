class Solution:
    def minimumChairs(self, s: str) -> int:
        occupied = answer = 0
        for event in s:
            if event == "E":
                occupied += 1
                answer = max(answer, occupied)
            else:
                occupied -= 1
        return answer


if __name__ == "__main__":
    test_cases = [("EEEE", 4), ("ELELE", 1), ("ELEELE", 2)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().minimumChairs(s) == expected
