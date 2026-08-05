"""2612. 最少翻转操作数"""


class Solution:
    def minReverseOperations(
        self, n: int, p: int, banned: list[int], k: int
    ) -> list[int]:
        from collections import deque

        parent = []
        for parity in range(2):
            size = (n - parity + 1) // 2
            parent.append(list(range(size + 1)))

        def find(parity, index):
            while parent[parity][index] != index:
                parent[parity][index] = parent[parity][parent[parity][index]]
                index = parent[parity][index]
            return index

        def remove(index):
            parity = index & 1
            parent[parity][index // 2] = find(parity, index // 2 + 1)

        for index in banned:
            remove(index)
        remove(p)
        answer = [-1] * n
        answer[p] = 0
        queue = deque([p])
        while queue:
            index = queue.popleft()
            low = max(0, index - k + 1)
            high = min(n - 1, index + k - 1)
            parity = (index + k - 1) & 1
            first = (low + (parity ^ (low & 1))) // 2
            current = find(parity, first)
            while current * 2 + parity <= high:
                next_index = current * 2 + parity
                answer[next_index] = answer[index] + 1
                queue.append(next_index)
                parent[parity][current] = find(parity, current + 1)
                current = find(parity, current)
        return answer


if __name__ == "__main__":
    test_cases = [((4, 0, [1, 2], 4), [0, -1, -1, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minReverseOperations(*args) == expected
