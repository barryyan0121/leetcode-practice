"""1834. 单线程 CPU"""

import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        ordered = sorted(
            (start, duration, index) for index, (start, duration) in enumerate(tasks)
        )
        answer = []
        heap = []
        time = 0
        position = 0
        while position < len(ordered) or heap:
            if not heap:
                time = max(time, ordered[position][0])
            while position < len(ordered) and ordered[position][0] <= time:
                start, duration, index = ordered[position]
                heapq.heappush(heap, (duration, index))
                position += 1
            duration, index = heapq.heappop(heap)
            answer.append(index)
            time += duration
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[1, 2], [2, 4], [3, 2], [4, 1]],), [0, 2, 3, 1]),
        (([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]],), [4, 3, 2, 0, 1]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().getOrder(*args) == expected
