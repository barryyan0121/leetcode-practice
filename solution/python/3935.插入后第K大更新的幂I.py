"""3935. 插入后第 K 大更新的幂 I"""

import heapq


class Solution:
    def powerUpdate(
        self, nums: list[int], p: int, queries: list[list[int]]
    ) -> list[int]:
        top = []
        rest = []
        for value in nums:
            heapq.heappush(rest, -value)
        answer = []
        mod = 1_000_000_007
        for value, k in queries:
            if top and value >= top[0]:
                heapq.heappush(top, value)
            else:
                heapq.heappush(rest, -value)
            while len(top) > k:
                heapq.heappush(rest, -heapq.heappop(top))
            while len(top) < k:
                heapq.heappush(top, -heapq.heappop(rest))
            p = pow(p, top[0], mod)
            answer.append(p)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([2], 4, [[3, 1], [1, 2]]), [64, 4096]),
        (([7, 5], 6, [[4, 3], [7, 2]]), [1296, 220296870]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().powerUpdate(*args) == expected
