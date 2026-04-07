#
# @lc app=leetcode.cn id=284 lang=python3
# @lcpr version=30203
#
# [284] 顶端迭代器
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._has_next = iterator.hasNext()
        self._next = iterator.next() if self._has_next else None

    def peek(self):
        return self._next

    def next(self):
        cur = self._next
        if self._has_next:
            self._has_next = self.iterator.hasNext()
            self._next = self.iterator.next() if self._has_next else None
        return cur

    def hasNext(self):
        return self._has_next
        # @lc code=end


if __name__ == "__main__":
    class SimpleIterator:
        def __init__(self, nums):
            self.nums = nums
            self.idx = 0

        def next(self):
            val = self.nums[self.idx]
            self.idx += 1
            return val

        def hasNext(self):
            return self.idx < len(self.nums)

    # 测试用例 (func, args, result)
    test_cases = [
        (
            [("init", [[1, 2, 3]]), ("peek", []), ("next", []), ("next", []), ("peek", []), ("next", []), ("hasNext", [])],
            [None, 1, 1, 2, 3, 3, False],
        ),
        (
            [("init", [[1]]), ("peek", []), ("hasNext", []), ("next", []), ("hasNext", [])],
            [None, 1, True, 1, False],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            obj = None
            for op, args in ops:
                if op == "init":
                    obj = PeekingIterator(SimpleIterator(*args))
                    result.append(None)
                elif op == "peek":
                    result.append(obj.peek())
                elif op == "next":
                    result.append(obj.next())
                else:
                    result.append(obj.hasNext())
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {ops}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {ops}, 期望 = {expected}, 实际 = {result}"
            )

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
# ["PeekingIterator","peek","next","next","hasNext"]\n[[[1,2,3]],[],[],[],[]]\n
# @lcpr case=end

#
