"""2260. 必须拿起的最小连续卡牌数"""


class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        last = {}
        answer = len(cards) + 1
        for i, value in enumerate(cards):
            if value in last:
                answer = min(answer, i - last[value] + 1)
            last[value] = i
        return answer if answer <= len(cards) else -1
