#
# @lc app=leetcode.cn id=855 lang=python3
#
# [855] 考场就座
#

import os
import sys
from bisect import insort


# @lc code=start
class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            seat = 0
        else:
            seat = 0
            distance = self.students[0]
            for left, right in zip(self.students, self.students[1:]):
                middle_distance = (right - left) // 2
                if middle_distance > distance:
                    distance = middle_distance
                    seat = left + middle_distance
            if self.n - self.students[-1] - 1 > distance:
                seat = self.n - 1
        insort(self.students, seat)
        return seat

    def leave(self, p: int) -> None:
        self.students.remove(p)


# @lc code=end


def run_operations(n, operations):
    room = ExamRoom(n)
    result = []
    for operation, value in operations:
        if operation == "seat":
            result.append(room.seat())
        else:
            room.leave(value)
            result.append(None)
    return result


if __name__ == "__main__":
    test_cases = [
        (
            run_operations,
            (
                10,
                [
                    ("seat", None),
                    ("seat", None),
                    ("seat", None),
                    ("seat", None),
                    ("leave", 4),
                    ("seat", None),
                ],
            ),
            [0, 9, 4, 2, None, 5],
        ),
        (run_operations, (1, [("seat", None)]), [0]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
