"""2059. 转化数字的最少操作次数"""

from collections import deque


class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        distance = [-1] * 1001
        distance[start] = 0
        queue = deque([start])
        while queue:
            value = queue.popleft()
            for number in nums:
                for next_value in (value + number, value - number, value ^ number):
                    if next_value == goal:
                        return distance[value] + 1
                    if 0 <= next_value <= 1000 and distance[next_value] < 0:
                        distance[next_value] = distance[value] + 1
                        queue.append(next_value)
        return -1


if __name__ == "__main__":
    test_cases = [(([2, 4, 12], 2, 12), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumOperations(*args) == expected
