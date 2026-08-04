class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        extended = colors + colors[: k - 1]
        run = 1
        answer = 0
        for index in range(1, len(extended)):
            if extended[index] != extended[index - 1]:
                run += 1
            else:
                run = 1
            if index >= k - 1 and run >= k:
                answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (([0, 1, 0, 1, 0], 3), 3),
        (([0, 1, 0, 0, 1, 0, 1], 6), 2),
        (([1, 1, 0, 1], 4), 0),
    ]
    for _, ((colors, k), expected) in enumerate(test_cases):
        assert Solution().numberOfAlternatingGroups(colors, k) == expected
