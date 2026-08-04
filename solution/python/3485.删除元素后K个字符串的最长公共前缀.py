"""3485. 删除元素后 K 个字符串的最长公共前缀"""


class Solution:
    def longestCommonPrefix(self, words: list[str], k: int) -> list[int]:
        dovranimex = (words, k)
        children = [{}]
        counts = [0]
        depths = [0]
        paths = []
        for word in words:
            node = 0
            path = []
            for char in word:
                if char not in children[node]:
                    children[node][char] = len(children)
                    children.append({})
                    counts.append(0)
                    depths.append(depths[node] + 1)
                node = children[node][char]
                counts[node] += 1
                path.append(node)
            paths.append(path)

        max_depth = max(depths)
        qualifying = [0] * (max_depth + 1)
        current_max = 0
        for node in range(1, len(children)):
            if counts[node] >= k:
                depth = depths[node]
                qualifying[depth] += 1
                current_max = max(current_max, depth)

        answer = []
        for path in paths:
            if len(words) - 1 < k:
                answer.append(0)
                continue
            for node in path:
                if counts[node] == k:
                    qualifying[depths[node]] -= 1
                counts[node] -= 1
            while current_max and qualifying[current_max] == 0:
                current_max -= 1
            answer.append(current_max)
            for node in path:
                if counts[node] == k - 1:
                    qualifying[depths[node]] += 1
                    current_max = max(current_max, depths[node])
                counts[node] += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        ((["jump", "run", "run", "jump", "run"], 2), [3, 4, 4, 3, 4]),
        ((["dog", "racer", "car"], 2), [0, 0, 0]),
    ]
    for _, ((words, k), expected) in enumerate(test_cases):
        assert Solution().longestCommonPrefix(words, k) == expected
