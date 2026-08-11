class Solution:
    def minimumTime(self, hens, grains):
        hens.sort()
        grains.sort()
        def can(t):
            i = 0
            for h in hens:
                if i == len(grains):
                    return True
                if grains[i] > h:
                    right = h + t
                else:
                    d = h - grains[i]
                    if d > t:
                        continue
                    right = max(h + t - 2 * d, h + (t - d) // 2)
                while i < len(grains) and grains[i] <= right:
                    i += 1
            return i == len(grains)
        lo, hi = 0, 10 ** 9
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
