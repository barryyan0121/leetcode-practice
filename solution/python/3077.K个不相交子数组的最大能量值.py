from typing import List


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        neg = -(10**30)
        out = [neg] * (k + 1)
        inside = [neg] * (k + 1)
        out[0] = 0
        for v in nums:
            for j in range(k, 0, -1):
                coef = (k - j + 1) * (1 if j % 2 else -1)
                best = max(inside[j], out[j - 1], inside[j - 1])
                inside[j] = best + v * coef if best > neg // 2 else neg
                out[j] = max(out[j], inside[j])
        return max(out[k], inside[k])


if __name__ == "__main__":
    s = Solution()
    assert s.maximumStrength([1, 2, 3, -1, 2], 3) == 22
    assert s.maximumStrength([12, -2, -2, -2, -2], 5) == 64
    print("3077 ok")
