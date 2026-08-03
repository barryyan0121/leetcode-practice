# @lc app=leetcode.cn id=1606 lang=python3


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        import heapq

        size = 1
        while size < k:
            size <<= 1
        tree = [k] * (2 * size)
        for server in range(k):
            tree[size + server] = server
        for node in range(size - 1, 0, -1):
            tree[node] = min(tree[node * 2], tree[node * 2 + 1])

        def update(server: int, value: int) -> None:
            node = size + server
            tree[node] = value
            node //= 2
            while node:
                tree[node] = min(tree[node * 2], tree[node * 2 + 1])
                node //= 2

        def query(left: int, right: int) -> int:
            answer = k
            left += size
            right += size
            while left < right:
                if left & 1:
                    answer = min(answer, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    answer = min(answer, tree[right])
                left //= 2
                right //= 2
            return answer

        busy = []
        handled = [0] * k
        for index, start in enumerate(arrival):
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                update(server, server)
            position = query(index % k, k)
            if position == k:
                position = query(0, index % k)
            if position == k:
                continue
            update(position, k)
            handled[position] += 1
            heapq.heappush(busy, (start + load[index], position))
        maximum = max(handled)
        return [server for server, count in enumerate(handled) if count == maximum]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.busiestServers, (3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3]), [1])]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1606 题 "找到处理最多请求的服务器" 所有测试用例通过')
