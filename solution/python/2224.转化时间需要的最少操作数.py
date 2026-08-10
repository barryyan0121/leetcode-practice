"""2224. 转化时间需要的最少操作数"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        to_minutes = lambda value: int(value[:2]) * 60 + int(value[3:])
        difference = to_minutes(correct) - to_minutes(current)
        answer = 0
        for step in (60, 15, 5, 1):
            answer += difference // step
            difference %= step
        return answer
