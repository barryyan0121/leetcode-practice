import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(available)
        busy = []
        answer = []
        time = 0
        for index, task in enumerate(tasks):
            time = max(time, index)
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
            if not available:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))
            weight, index = heapq.heappop(available)
            heapq.heappush(busy, (time + task, weight, index))
            answer.append(index)
        return answer


if __name__ == "__main__":
    assert Solution().assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]
