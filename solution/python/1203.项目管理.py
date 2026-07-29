from collections import defaultdict, deque
from typing import List


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        for item in range(n):
            if group[item] == -1:
                group[item] = m
                m += 1

        item_graph, group_graph = defaultdict(list), defaultdict(list)
        item_degree, group_degree = [0] * n, [0] * m
        for item, previous_items in enumerate(beforeItems):
            for previous in previous_items:
                item_graph[previous].append(item)
                item_degree[item] += 1
                if group[previous] != group[item]:
                    group_graph[group[previous]].append(group[item])
                    group_degree[group[item]] += 1

        def topo(graph: dict, degree: List[int]) -> List[int]:
            queue = deque(index for index, value in enumerate(degree) if value == 0)
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 0:
                        queue.append(neighbor)
            return order if len(order) == len(degree) else []

        group_order = topo(group_graph, group_degree)
        item_order = topo(item_graph, item_degree)
        if not group_order or not item_order:
            return []
        items_by_group = defaultdict(list)
        for item in item_order:
            items_by_group[group[item]].append(item)
        return [
            item
            for current_group in group_order
            for item in items_by_group[current_group]
        ]


if __name__ == "__main__":
    test_cases = [
        (
            8,
            2,
            [-1, -1, 1, 0, 0, 1, 0, -1],
            [[], [6], [5], [6], [3, 6], [], [], []],
            [6, 3, 4, 5, 2, 0, 7, 1],
        )
    ]
    for _, (n, m, group, before_items, expected) in enumerate(test_cases):
        assert Solution().sortItems(n, m, group, before_items) == expected
