"""2350. 不可能得到的最短骰子序列"""


class Solution:
    def shortestSequence(self, rolls: list[int], k: int) -> int:
        seen = set()
        answer = 1
        for value in rolls:
            seen.add(value)
            if len(seen) == k:
                answer += 1
                seen.clear()
        return answer
