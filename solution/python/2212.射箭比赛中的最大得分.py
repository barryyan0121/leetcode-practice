"""2212. 射箭比赛中的最大得分"""


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        best_score, best_mask = -1, 0
        for mask in range(1 << 12):
            arrows = sum(aliceArrows[i] + 1 for i in range(12) if mask >> i & 1)
            if arrows > numArrows:
                continue
            score = sum(i for i in range(12) if mask >> i & 1)
            if score > best_score:
                best_score, best_mask = score, mask
        answer = [0] * 12
        used = 0
        for i in range(12):
            if best_mask >> i & 1:
                answer[i] = aliceArrows[i] + 1
                used += answer[i]
        answer[0] += numArrows - used
        return answer
