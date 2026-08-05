"""3771. 探索地牢的得分"""

from bisect import bisect_left


class Solution:
    def totalScore(self, hp: int, damage: list[int], requirement: list[int]) -> int:
        prefix = [0]
        for value in damage:
            prefix.append(prefix[-1] + value)
        answer = 0
        for end, needed in enumerate(requirement):
            threshold = needed - hp + prefix[end + 1]
            answer += end + 1 - bisect_left(prefix, threshold, 0, end + 1)
        return answer


if __name__ == "__main__":
    test_cases = [((11, [3, 6, 7], [4, 2, 5]), 3), ((2, [10000, 1], [1, 1]), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().totalScore(*args) == expected
