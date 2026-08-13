from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if k <= 1:
            return 0
        times = sorted({t for _, _, t in edges})

        def components(t: int) -> int:
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(a, b):
                ra, rb = find(a), find(b)
                if ra != rb:
                    parent[rb] = ra

            comps = n
            for u, v, time in edges:
                if time > t:
                    if find(u) != find(v):
                        union(u, v)
                        comps -= 1
            return comps

        if components(0) >= k:
            return 0
        lo, hi = 0, times[-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if components(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.minTime(2, [[0, 1, 3]], 2) == 3
    assert s.minTime(3, [[0, 1, 2], [1, 2, 4]], 3) == 4
    assert s.minTime(3, [[0, 2, 5]], 2) == 0
    print("3608 ok")
