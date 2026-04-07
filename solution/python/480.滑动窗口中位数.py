#
# @lc app=leetcode.cn id=480 lang=python3
# @lcpr version=30203
#
# [480] 滑动窗口中位数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
import heapq
from collections import defaultdict
from common.node import *


class DualHeap:
    def __init__(self, k: int):
        self.small = []  # max heap (negative values)
        self.large = []  # min heap
        self.delayed = defaultdict(int)
        self.k = k
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap: List[int]) -> None:
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed[num]:
                heapq.heappop(heap)
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
            else:
                break

    def make_balance(self) -> None:
        if self.small_size > self.large_size + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large)

    def insert(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.make_balance()

    def erase(self, num: int) -> None:
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)
        self.make_balance()

    def get_median(self) -> float:
        if self.k % 2:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


# @lc code=start
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)
        ans = [dh.get_median()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.get_median())
        return ans
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.medianSlidingWindow,
            [[1, 3, -1, -3, 5, 3, 6, 7], 3],
            [1, -1, -1, 3, 5, 6],
        ),
        (solution.medianSlidingWindow, [[1, 4, 2, 3], 4], [2.5]),
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
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

#
