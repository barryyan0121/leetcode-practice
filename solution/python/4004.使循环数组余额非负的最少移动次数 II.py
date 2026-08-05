"""4004. 使循环数组余额非负的最少移动次数 II"""

import heapq


class Solution:
    def minMoves(self, balance: list[int]) -> int:
        if sum(balance) < 0:
            return -1
        n = len(balance)
        source, sink = n, n + 1
        graph = [[] for _ in range(n + 2)]

        def add_edge(left, right, capacity, cost):
            graph[left].append([right, capacity, cost, len(graph[right])])
            graph[right].append([left, 0, -cost, len(graph[left]) - 1])

        demand = 0
        for index, value in enumerate(balance):
            if value > 0:
                add_edge(source, index, value, 0)
            elif value < 0:
                demand -= value
                add_edge(index, sink, -value, 0)
            add_edge(index, (index + 1) % n, 10**18, 1)
            add_edge(index, (index - 1) % n, 10**18, 1)
        if demand == 0:
            return 0
        potential = [0] * (n + 2)
        answer = flow = 0
        while flow < demand:
            distances = [10**30] * (n + 2)
            previous = [None] * (n + 2)
            distances[source] = 0
            queue = [(0, source)]
            while queue:
                distance, node = heapq.heappop(queue)
                if distance != distances[node]:
                    continue
                for edge_index, edge in enumerate(graph[node]):
                    target, capacity, cost, _ = edge
                    if capacity <= 0:
                        continue
                    next_distance = (
                        distance + cost + potential[node] - potential[target]
                    )
                    if next_distance < distances[target]:
                        distances[target] = next_distance
                        previous[target] = (node, edge_index)
                        heapq.heappush(queue, (next_distance, target))
            if previous[sink] is None:
                return -1
            for node in range(n + 2):
                if distances[node] < 10**30:
                    potential[node] += distances[node]
            amount = demand - flow
            node = sink
            while node != source:
                parent, edge_index = previous[node]
                amount = min(amount, graph[parent][edge_index][1])
                node = parent
            node = sink
            while node != source:
                parent, edge_index = previous[node]
                edge = graph[parent][edge_index]
                edge[1] -= amount
                graph[node][edge[3]][1] += amount
                node = parent
            flow += amount
            answer += amount * potential[sink]
        return answer


if __name__ == "__main__":
    test_cases = [(([-1, 2, -1],), 2), (([4, -1, -2],), 3), (([-3, -3, 5],), -1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minMoves(*args) == expected
