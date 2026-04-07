#
# @lc app=leetcode.cn id=362 lang=python3
# @lcpr version=30203
#
# [362] 敲击计数器
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class HitCounter:
    def __init__(self):
        self.q = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0][0] <= timestamp - 300:
            ts, cnt = self.q.popleft()
            self.total -= cnt
        return self.total


# @lc code=end


if __name__ == "__main__":
    counter = HitCounter()

    def run_ops(ops: List[Tuple[str, int]]) -> List[Optional[int]]:
        obj = HitCounter()
        res = []
        for op, val in ops:
            if op == "hit":
                obj.hit(val)
                res.append(None)
            else:
                res.append(obj.getHits(val))
        return res

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_ops,
            [[("hit", 1), ("hit", 2), ("hit", 3), ("get", 4), ("hit", 300), ("get", 300), ("get", 301)]],
            [None, None, None, 3, None, 4, 3],
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
# ["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]\n
# [[],[1],[2],[3],[4],[300],[300],[301]]\n
# @lcpr case=end

#
