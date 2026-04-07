#
# @lc app=leetcode.cn id=358 lang=python3
# @lcpr version=30203
#
# [358] K 距离间隔重排字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from collections import Counter, deque
from heapq import heappush, heappop


# @lc code=start
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        counter = Counter(s)
        heap = [(-cnt, ch) for ch, cnt in counter.items()]
        import heapq

        heapq.heapify(heap)
        queue = deque()
        result = []
        time = 0

        while heap or queue:
            time += 1
            while queue and queue[0][2] <= time:
                cnt2, ch2, _ = queue.popleft()
                heapq.heappush(heap, (cnt2, ch2))

            if not heap:
                return ""

            cnt, ch = heapq.heappop(heap)
            result.append(ch)
            cnt += 1
            if cnt < 0:
                queue.append((cnt, ch, time + k))

        return "".join(result)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.rearrangeString, ("aabbcc", 3), "abcabc"),
        (solution.rearrangeString, ("aaabc", 3), ""),
        (solution.rearrangeString, ("aaadbbcc", 2), "abacabcd"),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            if expected:
                assert result and sorted(result) == sorted(args[0])
                assert all(
                    abs(i - j) >= args[1]
                    for i, ch1 in enumerate(result)
                    for j, ch2 in enumerate(result)
                    if i < j and ch1 == ch2
                )
            else:
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
# "aabbcc"\n3\n
# @lcpr case=end
