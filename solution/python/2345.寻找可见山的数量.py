"""2345. 寻找可见山的数量"""


from collections import Counter


class Solution:
    def visibleMountains(self, peaks: list[list[int]]) -> int:
        counts = Counter((x - y, x + y) for x, y in peaks)
        intervals = sorted(
            ((left, right, counts[(left, right)]) for left, right in counts),
            key=lambda item: (item[0], -item[1]),
        )
        answer = 0
        max_right = -1
        for left, right, count in intervals:
            if count == 1 and max_right < right:
                answer += 1
            max_right = max(max_right, right)
        return answer
