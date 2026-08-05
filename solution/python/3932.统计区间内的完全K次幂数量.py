"""3932. 统计区间内的完全 K 次幂数量"""


class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        velnacqori = l
        if k == 1:
            return r - velnacqori + 1

        def count(limit: int) -> int:
            if limit < 0:
                return 0
            total = 0
            value = 0
            while value**k <= limit:
                total += 1
                value += 1
            return total

        return count(r) - count(velnacqori - 1)


if __name__ == "__main__":
    test_cases = [((1, 9, 3), 2), ((8, 30, 2), 3), ((0, 0, 2), 1)]
    for _, ((l, r, k), expected) in enumerate(test_cases):
        assert Solution().countKthRoots(l, r, k) == expected
