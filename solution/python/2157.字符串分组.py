"""2157. 字符串分组"""


class Solution:
    def groupStrings(self, words: list[str]) -> list[int]:
        parent = {}

        def find(x: int) -> int:
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            x, y = find(x), find(y)
            if x != y:
                parent[x] = y

        owners = {}
        for word in words:
            mask = sum(1 << (ord(char) - 97) for char in word)
            owners[mask] = owners.get(mask, 0) + 1
        for mask in owners:
            for bit in range(26):
                if mask >> bit & 1:
                    base = mask ^ (1 << bit)
                    if base in owners:
                        union(mask, base)
                    for other in range(26):
                        if not mask >> other & 1 and (base | 1 << other) in owners:
                            union(mask, base | 1 << other)
        roots = {find(mask) for mask in owners}
        sizes = {root: 0 for root in roots}
        for mask in owners:
            sizes[find(mask)] += owners[mask]
        return [len(roots), max(sizes.values())]


if __name__ == "__main__":
    test_cases = [((["a", "b", "ab", "cde"],), [2, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().groupStrings(*args) == expected
