#
# @lc app=leetcode.cn id=981 lang=python3
#
# [981] 基于时间的键值存储
#

import os
import sys
from bisect import bisect_right
from collections import defaultdict


# @lc code=start
class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.data[key]
        index = bisect_right(entries, (timestamp, "\U0010ffff")) - 1
        return entries[index][1] if index >= 0 else ""


# @lc code=end


if __name__ == "__main__":
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    test_cases = [
        (time_map.get, ("foo", 1), "bar"),
        (time_map.get, ("foo", 3), "bar"),
        (time_map.get, ("foo", 0), ""),
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
