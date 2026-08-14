class Solution:
    def countNumbers(self, n: int, k: int) -> int:
        def depth(x):
            d = 0
            while x > 1:
                x = x.bit_count()
                d += 1
            return d

        bits = n.bit_length()
        comb = [[0] * (bits + 1) for _ in range(bits + 1)]
        for i in range(bits + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]

        def count_at_most(limit, ones):
            if ones < 0 or ones > bits:
                return 0
            ans = 0
            used = 0
            for i in range(bits - 1, -1, -1):
                if limit & (1 << i):
                    if ones - used <= i:
                        ans += comb[i][ones - used]
                    used += 1
                    if used > ones:
                        break
            return ans + (used == ones)

        if k == 0:
            return 1 if n >= 1 else 0

        ans = 0
        for ones in range(1, bits + 1):
            if depth(ones) == k - 1:
                ans += count_at_most(n, ones)
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.countNumbers(4, 1) == 2
    assert s.countNumbers(7, 2) == 3
    assert s.countNumbers(1, 0) == 1
    print("3621 ok")
