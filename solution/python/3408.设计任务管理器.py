import heapq


class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.tasks = {}
        self.heap = []
        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        user_id, _ = self.tasks[taskId]
        self.tasks[taskId] = (user_id, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, user_id))

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, negative_task_id, user_id = heapq.heappop(self.heap)
            task_id = -negative_task_id
            if self.tasks.get(task_id) == (user_id, -priority):
                del self.tasks[task_id]
                return user_id
        return -1


if __name__ == "__main__":
    test_cases = [
        ([[1, 101, 10], [2, 102, 20], [3, 103, 15]], [1, 3]),
    ]
    for _, (tasks, expected) in enumerate(test_cases):
        manager = TaskManager(tasks)
        manager.add(4, 104, 5)
        manager.edit(101, 25)
        actual = [manager.execTop()]
        manager.rmv(102)
        actual.append(manager.execTop())
        assert actual == expected
