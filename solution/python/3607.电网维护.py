from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maintenance(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        parent = list(range(c + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for u, v in connections:
            union(u, v)

        heaps = defaultdict(list)
        online = [True] * (c + 1)
        for i in range(1, c + 1):
            heappush(heaps[find(i)], i)

        ans = []
        for t, x in queries:
            root = find(x)
            if t == 2:
                online[x] = False
            else:
                if online[x]:
                    ans.append(x)
                else:
                    heap = heaps[root]
                    while heap and not online[heap[0]]:
                        heappop(heap)
                    ans.append(heap[0] if heap else -1)
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.maintenance(
        5, [[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
    ) == [3, 2, 3]
    assert s.maintenance(3, [], [[1, 1], [2, 1], [1, 1]]) == [1, -1]
    print("3607 ok")
