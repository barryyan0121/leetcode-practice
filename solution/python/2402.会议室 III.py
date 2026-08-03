# @lc app=leetcode.cn id=2402 lang=python3

import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        available = list(range(n))
        heapq.heapify(available)
        busy = []
        used = [0] * n
        for start, end in sorted(meetings):
            duration = end - start
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            if available:
                room = heapq.heappop(available)
                finish = end
            else:
                finish, room = heapq.heappop(busy)
                finish += duration
            used[room] += 1
            heapq.heappush(busy, (finish, room))
        return max(range(n), key=lambda room: (used[room], -room))


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.mostBooked, (2, [[0, 10], [1, 5], [2, 7], [3, 4]]), 0),
        (solution.mostBooked, (3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2402 题 "会议室 III" 所有测试用例通过')
