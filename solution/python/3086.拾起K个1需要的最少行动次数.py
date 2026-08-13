class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        pos = [i for i, v in enumerate(nums) if v]
        n = len(pos)
        lo, hi = max(0, k - maxChanges), min(k, n)
        pref = [0]
        for x in pos:
            pref.append(pref[-1] + x)
        ans = 2 * k
        for cnt in range(max(1, lo), hi + 1):
            for l in range(n - cnt + 1):
                r = l + cnt - 1
                m = (l + r) // 2
                left = pos[m] * (m - l) - (pref[m] - pref[l])
                right = pref[r + 1] - pref[m + 1] - pos[m] * (r - m)
                ans = min(ans, left + right + 2 * (k - cnt))
        return ans
