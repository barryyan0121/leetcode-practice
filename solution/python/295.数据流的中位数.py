#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30203
#
# [295] 数据流的中位数
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


# @lc code=end


if __name__ == "__main__":
    mf = MedianFinder()

    def run_ops(ops: List[Tuple[str, Optional[int]]]) -> List[Optional[float]]:
        obj = MedianFinder()
        res = []
        for op, val in ops:
            if op == "add":
                obj.addNum(val)
                res.append(None)
            else:
                res.append(obj.findMedian())
        return res

    # 测试用例 (func, args, result)
    test_cases = [
        (run_ops, [[("add", 1), ("add", 2), ("find", None), ("add", 3), ("find", None)]], [None, None, 1.5, None, 2.0]),
        (run_ops, [[("add", 2), ("find", None)]], [None, 2.0]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
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
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n
# [[],[1],[2],[],[3],[]]\n
# @lcpr case=end

#
