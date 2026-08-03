# @lc app=leetcode.cn id=1354 lang=python3

import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-value for value in target]
        heapq.heapify(heap)
        while -heap[0] != 1:
            largest = -heapq.heappop(heap)
            rest = total - largest
            if rest <= 0 or largest <= rest:
                return False
            if rest == 1:
                return True
            previous = largest % rest
            if previous == 0:
                return False
            total = rest + previous
            heapq.heappush(heap, -previous)
        return True


if __name__ == "__main__":
    test_cases = [
        (Solution().isPossible, ([9, 3, 5],), True),
        (Solution().isPossible, ([1, 1, 1, 2],), False),
        (Solution().isPossible, ([8, 5],), True),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1354 题 "多次求和构造目标数组" 所有测试用例通过')
