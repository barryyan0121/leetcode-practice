from collections import deque
from typing import List


class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        dist = [-1] * (1 << m)
        q = deque()
        for x in nums:
            if dist[x] == -1:
                dist[x] = 0
                q.append(x)
        while q:
            x = q.popleft()
            for i in range(m):
                y = x ^ (1 << i)
                if dist[y] == -1:
                    dist[y] = dist[x] + 1
                    q.append(y)
        mask = (1 << m) - 1
        return [m - dist[x ^ mask] for x in nums]


if __name__ == "__main__":
    assert Solution().maxHammingDistances([9, 12, 9, 11], 4) == [2, 3, 2, 3]
    assert Solution().maxHammingDistances([3, 4, 6, 10], 4) == [3, 3, 2, 3]
