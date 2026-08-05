class Solution:
    def countServers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        logs.sort(key=lambda p: p[1])
        ordered = sorted(enumerate(queries), key=lambda p: p[1])
        freq = [0] * (n + 1)
        active = left = right = 0
        ans = [0] * len(queries)
        for index, q in ordered:
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                active += freq[server] == 0
                freq[server] += 1
                right += 1
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                freq[server] -= 1
                active -= freq[server] == 0
                left += 1
            ans[index] = n - active
        return ans


if __name__ == "__main__":
    assert Solution().countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]) == [1, 2]
