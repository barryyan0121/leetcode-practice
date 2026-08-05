"""3590. 第 K 小的路径异或和"""

import sys
from collections import defaultdict


class Solution:
    def kthSmallest(
        self, par: list[int], vals: list[int], queries: list[list[int]]
    ) -> list[int]:
        narvetholi = queries
        sys.setrecursionlimit(300000)
        n = len(vals)
        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[par[node]].append(node)
        xor_value = [0] * n
        xor_value[0] = vals[0]
        traversal = [0]
        for node in traversal:
            for child in children[node]:
                xor_value[child] = xor_value[node] ^ vals[child]
                traversal.append(child)
        size = [1] * n
        heavy = [-1] * n
        tin = [0] * n
        tout = [0] * n
        euler = []
        timer = 0

        def prepare(node):
            nonlocal timer
            tin[node] = timer
            euler.append(node)
            timer += 1
            largest = 0
            for child in children[node]:
                prepare(child)
                size[node] += size[child]
                if size[child] > largest:
                    largest, heavy[node] = size[child], child
            tout[node] = timer

        prepare(0)
        grouped = defaultdict(list)
        for index, (node, order) in enumerate(narvetholi):
            grouped[node].append((order, index))

        left_child = [0]
        right_child = [0]
        counts = [0]
        frequencies = defaultdict(int)
        active = set()

        def change(value, delta):
            old = frequencies[value]
            new = old + delta
            frequencies[value] = new
            if old == 0 and new == 1:
                node = 0
                counts[node] += 1
                for bit in range(16, -1, -1):
                    branch = (value >> bit) & 1
                    if branch:
                        nxt = right_child[node]
                        if not nxt:
                            nxt = len(counts)
                            right_child[node] = nxt
                            left_child.append(0)
                            right_child.append(0)
                            counts.append(0)
                    else:
                        nxt = left_child[node]
                        if not nxt:
                            nxt = len(counts)
                            left_child[node] = nxt
                            left_child.append(0)
                            right_child.append(0)
                            counts.append(0)
                    node = nxt
                    counts[node] += 1
            elif old == 1 and new == 0:
                node = 0
                counts[node] -= 1
                for bit in range(16, -1, -1):
                    node = right_child[node] if (value >> bit) & 1 else left_child[node]
                    counts[node] -= 1
                del frequencies[value]

        def add_subtree(node, delta):
            for index in range(tin[node], tout[node]):
                change(xor_value[euler[index]], delta)

        answer = [-1] * len(queries)

        def kth(order):
            if order > counts[0]:
                return -1
            node = 0
            value = 0
            for bit in range(16, -1, -1):
                left = left_child[node]
                if left and counts[left] >= order:
                    node = left
                else:
                    if left:
                        order -= counts[left]
                    node = right_child[node]
                    value |= 1 << bit
            return value

        def solve(node, keep):
            for child in children[node]:
                if child != heavy[node]:
                    solve(child, False)
            if heavy[node] != -1:
                solve(heavy[node], True)
            for child in children[node]:
                if child != heavy[node]:
                    add_subtree(child, 1)
            change(xor_value[node], 1)
            for order, index in grouped[node]:
                answer[index] = kth(order)
            if not keep:
                add_subtree(node, -1)

        solve(0, True)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([-1, 0, 0], [1, 1, 1], [[0, 1], [0, 2], [0, 3]]), [0, 1, -1]),
        (([-1, 0, 1], [5, 2, 7], [[0, 1], [1, 2], [1, 3], [2, 1]]), [0, 7, -1, 0]),
    ]
    for _, ((par, vals, queries), expected) in enumerate(test_cases):
        assert Solution().kthSmallest(par, vals, queries) == expected
