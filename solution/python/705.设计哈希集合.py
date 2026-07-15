#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

import os
import sys


# @lc code=start
class MyHashSet:
    def __init__(self):
        self.present = bytearray(1_000_001)

    def add(self, key: int) -> None:
        self.present[key] = 1

    def remove(self, key: int) -> None:
        self.present[key] = 0

    def contains(self, key: int) -> bool:
        return bool(self.present[key])


# @lc code=end


if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    test_cases = [
        (obj.contains, (1,), True),
        (obj.contains, (3,), False),
        (obj.remove, (2,), None),
        (obj.contains, (2,), False),
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
