class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        chosen = set()
        value = 1
        ans = 0
        while len(chosen) < n:
            if k - value not in chosen:
                chosen.add(value)
                ans += value
            value += 1
        return ans


if __name__ == "__main__":
    assert Solution().minimumSum(5, 4) == 18
