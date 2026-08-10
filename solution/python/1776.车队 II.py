from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = [-1.0] * len(cars)
        stack = []
        for i in range(len(cars) - 1, -1, -1):
            position, speed = cars[i]
            while stack:
                j = stack[-1]
                next_position, next_speed = cars[j]
                if speed <= next_speed:
                    stack.pop()
                    continue
                time = (next_position - position) / (speed - next_speed)
                if result[j] < 0 or time <= result[j]:
                    result[i] = time
                    break
                stack.pop()
            stack.append(i)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.getCollisionTimes([[1, 2], [2, 1], [4, 3], [7, 2]]) == [
        1.0,
        -1.0,
        3.0,
        -1.0,
    ]
    print("1776 passed")
