"""2092. 找出知晓秘密的所有专家"""


class Solution:
    def findAllPeople(
        self, n: int, meetings: list[list[int]], firstPerson: int
    ) -> list[int]:
        meetings.sort(key=lambda meeting: meeting[2])
        knows = {0, firstPerson}
        index = 0
        while index < len(meetings):
            end = index
            time = meetings[index][2]
            graph = {}
            while end < len(meetings) and meetings[end][2] == time:
                x, y, _ = meetings[end]
                graph.setdefault(x, []).append(y)
                graph.setdefault(y, []).append(x)
                end += 1
            queue = [node for node in graph if node in knows]
            seen = set(queue)
            for node in queue:
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            knows.update(seen)
            index = end
        return list(knows)


if __name__ == "__main__":
    test_cases = [((6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1), [0, 1, 2, 3, 5])]
    for _, (args, expected) in enumerate(test_cases):
        assert sorted(Solution().findAllPeople(*args)) == expected
