from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must = [(u, v, s) for u, v, s, m in edges if m]
        opt = [(u, v, s) for u, v, s, m in edges if not m]
        hi = max((s * 2 for _, _, s in opt), default=0)
        hi = max(hi, max((s for _, _, s in must), default=0))

        def check(target: int) -> bool:
            if any(s < target for _, _, s in must):
                return False

            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(a, b):
                ra, rb = find(a), find(b)
                if ra == rb:
                    return False
                parent[rb] = ra
                return True

            comps = n
            for u, v, _ in must:
                if union(u, v):
                    comps -= 1
                else:
                    return False

            for u, v, s in opt:
                if s >= target and union(u, v):
                    comps -= 1

            if comps == 1:
                return True

            upgrades = 0
            for u, v, s in opt:
                if s < target <= s * 2 and union(u, v):
                    upgrades += 1
                    comps -= 1
                    if comps == 1:
                        return upgrades <= k
            return comps == 1 and upgrades <= k

        if not check(1):
            return -1
        lo, hi = 1, hi
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.maxStability(3, [[0, 1, 2, 1], [1, 2, 3, 0]], 1) == 2
    assert s.maxStability(3, [[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]], 2) == 4
    print("3600 ok")
