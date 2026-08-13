from bisect import bisect_right
from itertools import accumulate


class Solution:
    def countTasks(self, tasks: list[int], shifts: list[int]) -> list[int]:
        drelvanito = (tasks, shifts)
        prefix = [0, *accumulate(tasks)]
        total = prefix[-1]
        completed = 0
        answer = []
        for shift in shifts:
            completed += shift
            if completed >= total:
                answer.append(0)
                completed = 0
            else:
                finished = bisect_right(prefix, completed) - 1
                answer.append(len(tasks) - finished)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 4, 4], [9, 1, 4]), [0, 2, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countTasks(*args) == expected
