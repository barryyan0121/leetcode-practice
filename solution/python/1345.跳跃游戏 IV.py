# @lc app=leetcode.cn id=1345 lang=python3

from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        positions = defaultdict(list)
        for index, value in enumerate(arr):
            positions[value].append(index)
        queue, distance, used = deque([0]), {0: 0}, set()
        while queue:
            index = queue.popleft()
            if index == len(arr) - 1:
                return distance[index]
            candidates = [index - 1, index + 1]
            if arr[index] not in used:
                candidates += positions[arr[index]]
                used.add(arr[index])
            for next_index in candidates:
                if 0 <= next_index < len(arr) and next_index not in distance:
                    distance[next_index] = distance[index] + 1
                    queue.append(next_index)
        return -1


if __name__ == "__main__":
    test_cases = [
        (Solution().minJumps, ([100, -23, -23, 404, 100, 23, 23, 23, 3, 404],), 3),
        (Solution().minJumps, ([7],), 0),
        (Solution().minJumps, ([7, 6, 9, 6, 9, 6, 9, 7],), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1345 题 "跳跃游戏 IV" 所有测试用例通过')
