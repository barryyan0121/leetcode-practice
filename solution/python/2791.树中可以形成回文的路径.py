class Solution:
    def countPalindromePaths(self, parent: list[int], s: str) -> int:
        graph = [[] for _ in parent]
        for child in range(1, len(parent)):
            graph[parent[child]].append((child, 1 << (ord(s[child]) - 97)))
        counts = {0: 1}
        ans = 0

        def dfs(node: int, mask: int) -> None:
            nonlocal ans
            for child, bit in graph[node]:
                next_mask = mask ^ bit
                ans += counts.get(next_mask, 0)
                for j in range(26):
                    ans += counts.get(next_mask ^ (1 << j), 0)
                counts[next_mask] = counts.get(next_mask, 0) + 1
                dfs(child, next_mask)

        dfs(0, 0)
        return ans


if __name__ == "__main__":
    assert Solution().countPalindromePaths([-1, 0, 0, 1, 1, 2], "acaabc") == 8
