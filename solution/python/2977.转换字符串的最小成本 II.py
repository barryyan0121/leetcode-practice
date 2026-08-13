from heapq import heappop, heappush


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        words = set(original) | set(changed)
        ids = {word: index for index, word in enumerate(words)}
        graph = [[] for _ in words]
        for first, second, value in zip(original, changed, cost):
            graph[ids[first]].append((ids[second], value))
        distances = {}
        for start in set(original):
            source_id = ids[start]
            best = [10**30] * len(words)
            best[source_id] = 0
            heap = [(0, source_id)]
            while heap:
                value, node = heappop(heap)
                if value != best[node]:
                    continue
                for next_node, weight in graph[node]:
                    new_value = value + weight
                    if new_value < best[next_node]:
                        best[next_node] = new_value
                        heappush(heap, (new_value, next_node))
            distances[start] = best
        trie = {}
        for word in original:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[None] = word
        infinity = 10**30
        dp = [infinity] * (len(source) + 1)
        dp[0] = 0
        for index in range(len(source)):
            if dp[index] == infinity:
                continue
            if source[index] == target[index]:
                dp[index + 1] = min(dp[index + 1], dp[index])
            node = trie
            for end in range(index, len(source)):
                node = node.get(source[end])
                if node is None:
                    break
                if None in node and target[index : end + 1] in ids:
                    value = distances[node[None]][ids[target[index : end + 1]]]
                    if value < infinity:
                        dp[end + 1] = min(dp[end + 1], dp[index] + value)
        return -1 if dp[-1] == infinity else dp[-1]


if __name__ == "__main__":
    assert (
        Solution().minimumCost(
            "abcd",
            "acbe",
            ["a", "b", "c", "c", "e", "d"],
            ["b", "c", "b", "e", "b", "e"],
            [2, 5, 5, 1, 2, 20],
        )
        == 28
    )
