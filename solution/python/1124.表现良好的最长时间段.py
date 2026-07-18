class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        first = {0: -1}
        score = answer = 0
        for index, hour in enumerate(hours):
            score += 1 if hour > 8 else -1
            if score > 0:
                answer = index + 1
            else:
                first.setdefault(score, index)
                if score - 1 in first:
                    answer = max(answer, index - first[score - 1])
        return answer


if __name__ == "__main__":
    test_cases = [
        ([9, 9, 6, 0, 6, 6, 9], 3),
        ([6, 6, 6], 0),
        ([6, 9, 9], 3),
        ([9, 6, 6, 9, 9], 5),
    ]
    for _, (hours, expected) in enumerate(test_cases):
        assert Solution().longestWPI(hours) == expected
