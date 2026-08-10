"""2071. 你可以安排的最多任务数目"""

from collections import deque


class Solution:
    def maxTaskAssign(
        self, tasks: list[int], workers: list[int], pills: int, strength: int
    ) -> int:
        tasks.sort()
        workers.sort()

        def possible(count: int) -> bool:
            selected = workers[-count:]
            available = deque()
            task_index = 0
            used = 0
            for worker in selected:
                while task_index < count and tasks[task_index] <= worker + strength:
                    available.append(tasks[task_index])
                    task_index += 1
                if not available:
                    return False
                if available[0] <= worker:
                    available.popleft()
                elif used < pills:
                    used += 1
                    available.pop()
                else:
                    return False
            return True

        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            middle = (low + high + 1) // 2
            if possible(middle):
                low = middle
            else:
                high = middle - 1
        return low


if __name__ == "__main__":
    test_cases = [(([3, 2, 1], [0, 3, 3], 1, 1), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxTaskAssign(*args) == expected
