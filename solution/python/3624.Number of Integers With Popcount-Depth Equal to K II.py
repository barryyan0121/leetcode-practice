class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)


class Solution:
    def popcountDepthQueries(self, nums, queries):
        def depth(x):
            d = 0
            while x > 1:
                x = x.bit_count()
                d += 1
            return d

        ds = [depth(x) for x in nums]
        trees = [Fenwick(len(nums)) for _ in range(6)]
        for i, d in enumerate(ds):
            trees[d].add(i, 1)

        ans = []
        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                ans.append(trees[k].range_sum(l, r))
            else:
                _, idx, val = q
                trees[ds[idx]].add(idx, -1)
                ds[idx] = depth(val)
                trees[ds[idx]].add(idx, 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.popcountDepthQueries([2, 4], [[1, 0, 1, 1], [2, 1, 1], [1, 0, 1, 0]]) == [
        2,
        1,
    ]
    assert s.popcountDepthQueries(
        [3, 5, 6], [[1, 0, 2, 2], [2, 1, 4], [1, 1, 2, 1], [1, 0, 1, 0]]
    ) == [3, 1, 0]
    print("3624 ok")
