#
# @lc app=leetcode.cn id=460 lang=python3
# @lcpr version=30203
#
# [460] LFU 缓存
#

import sys
import os
from collections import defaultdict, OrderedDict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)

    def _increase_freq(self, key: int) -> None:
        value, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_to_val_freq[key] = (value, freq + 1)
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        value, _ = self.key_to_val_freq[key]
        self._increase_freq(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val_freq:
            _, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self._increase_freq(key)
            return
        if len(self.key_to_val_freq) == self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


# @lc code=end


if __name__ == "__main__":
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[int]]:
        obj = None
        result = []
        for op, value in zip(ops, values):
            if op == "LFUCache":
                obj = LFUCache(value[0])
                result.append(None)
            elif op == "put":
                obj.put(*value)
                result.append(None)
            elif op == "get":
                result.append(obj.get(value[0]))
        return result

    test_cases = [
        (
            run_operations,
            (
                ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
            ),
            [None, None, None, 1, None, -1, 3, None, -1, 3, 4],
        ),
        (
            run_operations,
            (
                ["LFUCache", "put", "get"],
                [[0], [0, 0], [0]],
            ),
            [None, None, -1],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]\n
# @lcpr case=end
