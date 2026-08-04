class Solution:
    def shiftDistance(
        self,
        s: str,
        t: str,
        nextCost: list[int],
        previousCost: list[int],
    ) -> int:
        answer = 0
        for source, target in zip(s, t):
            start = ord(source) - ord("a")
            end = ord(target) - ord("a")
            clockwise = 0
            index = start
            while index != end:
                clockwise += nextCost[index]
                index = (index + 1) % 26
            counterclockwise = 0
            index = start
            while index != end:
                counterclockwise += previousCost[index]
                index = (index - 1) % 26
            answer += min(clockwise, counterclockwise)
        return answer


if __name__ == "__main__":
    test_cases = [
        (("abab", "baba", [1] * 26, [1] * 26), 4),
        (("a", "c", [1] * 26, [10] * 26), 2),
    ]
    for _, ((s, t, next_cost, previous_cost), expected) in enumerate(test_cases):
        assert Solution().shiftDistance(s, t, next_cost, previous_cost) == expected
