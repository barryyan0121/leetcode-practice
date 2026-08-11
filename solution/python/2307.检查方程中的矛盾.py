class Solution:
    def checkContradictions(self, equations, values):
        graph = {}
        for (a, b), v in zip(equations, values):
            graph.setdefault(a, []).append((b, v))
            graph.setdefault(b, []).append((a, 1 / v))
        for start in graph:
            seen = {start: 1.0}
            stack = [start]
            while stack:
                u = stack.pop()
                for v, ratio in graph[u]:
                    value = seen[u] * ratio
                    if v in seen:
                        if abs(seen[v] - value) > 1e-5 * max(
                            1, abs(seen[v]), abs(value)
                        ):
                            return True
                    else:
                        seen[v] = value
                        stack.append(v)
        return False
