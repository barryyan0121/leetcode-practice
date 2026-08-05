"""2590. 设计一个待办事项清单"""


class TodoList:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def addTask(
        self, userId: int, taskDescription: str, dueDate: int, tags: list[str]
    ) -> int:
        task_id = self.next_id
        self.next_id += 1
        self.tasks[task_id] = [userId, taskDescription, dueDate, tags, False]
        return task_id

    def getAllTasks(self, userId: int) -> list[str]:
        return [
            task[1] for task in self.tasks.values() if task[0] == userId and not task[4]
        ]

    def getTasksForTag(self, userId: int, tag: str) -> list[str]:
        return [
            task[1]
            for task in self.tasks.values()
            if task[0] == userId and tag in task[3] and not task[4]
        ]

    def completeTask(self, userId: int, taskId: int) -> None:
        if taskId in self.tasks and self.tasks[taskId][0] == userId:
            self.tasks[taskId][4] = True


if __name__ == "__main__":
    test_cases = [((), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert expected
    todo = TodoList()
    task_id = todo.addTask(1, "a", 1, ["x"])
    assert todo.getTasksForTag(1, "x") == ["a"]
    todo.completeTask(1, task_id)
    assert todo.getAllTasks(1) == []
