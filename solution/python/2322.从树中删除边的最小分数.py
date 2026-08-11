class Solution:
    def minimumScore(self, nums, edges):
        n = len(nums)
        g = [[] for _ in nums]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        xor = [0] * n
        tin = [0] * n
        tout = [0] * n
        t = 0

        def dfs(u, p):
            nonlocal t
            tin[u] = t
            t += 1
            xor[u] = nums[u]
            for v in g[u]:
                if v != p:
                    dfs(v, u)
                    xor[u] ^= xor[v]
            tout[u] = t

        dfs(0, -1)
        total = xor[0]
        ans = 10**9
        for a in range(1, n):
            for b in range(a + 1, n):
                if tin[a] <= tin[b] < tout[a]:
                    x, y, z = xor[b], xor[a] ^ xor[b], total ^ xor[a]
                elif tin[b] <= tin[a] < tout[b]:
                    x, y, z = xor[a], xor[b] ^ xor[a], total ^ xor[b]
                else:
                    x, y, z = xor[a], xor[b], total ^ xor[a] ^ xor[b]
                ans = min(ans, max(x, y, z) - min(x, y, z))
        return ans
