"""2246. 相邻字符不同的最长路径"""


class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        children = [[] for _ in parent]
        for node in range(1, len(parent)):
            children[parent[node]].append(node)
        answer = 1

        def dfs(node: int) -> int:
            nonlocal answer
            longest = second = 0
            for child in children[node]:
                path = dfs(child)
                if s[child] == s[node]:
                    continue
                if path > longest:
                    longest, second = path, longest
                elif path > second:
                    second = path
            answer = max(answer, longest + second + 1)
            return longest + 1

        dfs(0)
        return answer


if __name__ == "__main__":
    assert Solution().longestPath([-1, 0, 0, 1, 1, 2], "abacbe") == 3
