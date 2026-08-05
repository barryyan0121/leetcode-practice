"""2534. 通过门的时间"""

from collections import deque


class Solution:
    def timeTaken(self, arrival: list[int], state: list[int]) -> list[int]:
        enter, leave = deque(), deque()
        answer = [0] * len(arrival)
        time = 0
        last = 1
        index = 0
        while index < len(arrival) or enter or leave:
            if not enter and not leave and index < len(arrival):
                time = max(time, arrival[index])
                last = 1
            while index < len(arrival) and arrival[index] <= time:
                (enter if state[index] == 0 else leave).append(index)
                index += 1
            queue = leave if last == 1 and leave else enter if enter else leave
            person = queue.popleft()
            answer[person] = time
            last = state[person]
            time += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([0, 0, 0, 0], [0, 1, 1, 0]), [2, 0, 1, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().timeTaken(*args) == expected
