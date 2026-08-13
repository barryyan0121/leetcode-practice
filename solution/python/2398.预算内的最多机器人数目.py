"""2398. 预算内的最多机器人数目"""

from collections import deque


class Solution:
    def maximumRobots(
        self, chargeTimes: list[int], runningCosts: list[int], budget: int
    ) -> int:
        queue = deque()
        left = total = answer = 0
        for right, cost in enumerate(runningCosts):
            total += cost
            while queue and chargeTimes[queue[-1]] <= chargeTimes[right]:
                queue.pop()
            queue.append(right)
            while queue and chargeTimes[queue[0]] + (right - left + 1) * total > budget:
                if queue[0] == left:
                    queue.popleft()
                total -= runningCosts[left]
                left += 1
            answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    assert Solution().maximumRobots([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25) == 3
