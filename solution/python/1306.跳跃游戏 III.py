# @lc app=leetcode.cn id=1306 lang=python3

from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue, seen = deque([start]), {start}
        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            for next_index in (index - arr[index], index + arr[index]):
                if 0 <= next_index < len(arr) and next_index not in seen:
                    seen.add(next_index)
                    queue.append(next_index)
        return False


if __name__ == "__main__":
    test_cases = [
        (Solution().canReach, ([4, 2, 3, 0, 3, 1, 2], 5), True),
        (Solution().canReach, ([4, 2, 3, 0, 3, 1, 2], 0), True),
        (Solution().canReach, ([3, 0, 2, 1, 2], 2), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1306 题 "跳跃游戏 III" 所有测试用例通过')
