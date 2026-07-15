#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

import os
import sys


# @lc code=start
class MyHashMap:
    def __init__(self):
        self.values = [-1] * 1_000_001

    def put(self, key: int, value: int) -> None:
        self.values[key] = value

    def get(self, key: int) -> int:
        return self.values[key]

    def remove(self, key: int) -> None:
        self.values[key] = -1


# @lc code=end


if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    test_cases = [
        (obj.get, (1,), 1),
        (obj.get, (3,), -1),
        (obj.put, (2, 1), None),
        (obj.get, (2,), 1),
        (obj.remove, (2,), None),
        (obj.get, (2,), -1),
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
