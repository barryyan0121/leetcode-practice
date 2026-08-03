# @lc app=leetcode.cn id=1298 lang=python3

from collections import deque
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        queue = deque(initialBoxes)
        have_box = set(initialBoxes)
        have_key = set()
        opened = set()
        total = 0
        while queue:
            box = queue.popleft()
            if box in opened or (status[box] == 0 and box not in have_key):
                continue
            opened.add(box)
            total += candies[box]
            for key in keys[box]:
                if key not in have_key:
                    have_key.add(key)
                    if key in have_box:
                        queue.append(key)
            for child in containedBoxes[box]:
                if child not in have_box:
                    have_box.add(child)
                queue.append(child)
        return total


if __name__ == "__main__":
    test_cases = [
        (
            Solution().maxCandies,
            (
                [1, 0, 1, 0],
                [7, 5, 4, 100],
                [[], [], [1], []],
                [[1, 2], [3], [], []],
                [0],
            ),
            16,
        ),
        (
            Solution().maxCandies,
            (
                [1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1],
                [[1, 2, 3, 4, 5], [], [], [], [], []],
                [[1, 2, 3, 4, 5], [], [], [], [], []],
                [0],
            ),
            6,
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1298 题 "你能从盒子里获得的最大糖果数" 所有测试用例通过')
