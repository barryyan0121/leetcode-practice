#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

import os
import sys
from collections import deque


# @lc code=start
class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)


# @lc code=end


def run_operations(times):
    counter = RecentCounter()
    return [counter.ping(time) for time in times]


if __name__ == "__main__":
    test_cases = [
        (run_operations, ([1, 100, 3001, 3002],), [1, 2, 3, 3]),
        (run_operations, ([1, 3001, 6001],), [1, 2, 2]),
        (run_operations, ([100],), [1]),
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
