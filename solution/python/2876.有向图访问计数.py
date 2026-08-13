class Solution:
    def countVisitedNodes(self, edges: list[int]) -> list[int]:
        n = len(edges)
        answer = [0] * n
        state = [0] * n

        def visit(start: int) -> None:
            path = []
            current = start
            while state[current] == 0:
                state[current] = 1
                path.append(current)
                current = edges[current]
            if state[current] == 1:
                cycle_start = path.index(current)
                cycle_length = len(path) - cycle_start
                for node in path[cycle_start:]:
                    answer[node] = cycle_length
                    state[node] = 2
                path = path[:cycle_start]
            while path:
                node = path.pop()
                answer[node] = answer[edges[node]] + 1
                state[node] = 2
            state[start] = 2

        for node in range(n):
            if state[node] == 0:
                visit(node)
        return answer


assert Solution().countVisitedNodes([1, 2, 0, 0]) == [3, 3, 3, 4]
