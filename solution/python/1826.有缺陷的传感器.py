"""1826. 有缺陷的传感器"""


class Solution:
    def badSensor(self, sensor1: list[int], sensor2: list[int]) -> int:
        first = next(
            (
                i
                for i, (left, right) in enumerate(zip(sensor1, sensor2))
                if left != right
            ),
            len(sensor1),
        )
        if first >= len(sensor1) - 1:
            return -1
        first_possible = sensor1[first:-1] == sensor2[first + 1 :]
        second_possible = sensor1[first + 1 :] == sensor2[first:-1]
        if first_possible and second_possible:
            return -1
        if first_possible:
            return 1
        if second_possible:
            return 2
        return -1


if __name__ == "__main__":
    test_cases = [
        (([2, 3, 4, 5], [2, 1, 3, 4]), 2),
        (([2, 3, 4, 5], [2, 3, 4, 5]), -1),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().badSensor(*args) == expected
