"""2555. 两个线段获得的最多奖品"""


class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        left = 0
        best = [0] * len(prizePositions)
        answer = 0
        for right, position in enumerate(prizePositions):
            while position - prizePositions[left] > k:
                left += 1
            previous = best[left - 1] if left else 0
            best[right] = max(best[right - 1] if right else 0, right - left + 1)
            answer = max(answer, previous + right - left + 1)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 0), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximizeWin(*args) == expected
