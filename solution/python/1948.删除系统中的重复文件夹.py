"""1948. 删除系统中的重复文件夹"""


class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        root = {}
        for path in paths:
            node = root
            for name in path:
                node = node.setdefault(name, {})
        serials = {}
        duplicate = set()

        def encode(node):
            key = tuple((name, encode(child)) for name, child in sorted(node.items()))
            if key:
                serials[key] = serials.get(key, 0) + 1
            return key

        encode(root)

        def shape(node):
            return tuple((name, shape(child)) for name, child in sorted(node.items()))

        def collect(node, path):
            key = shape(node)
            if key and serials[key] > 1:
                return
            if path:
                answer.append(path)
            for name, child in sorted(node.items()):
                collect(child, path + [name])

        answer = []
        collect(root, [])
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            (
                [
                    ["a"],
                    ["c"],
                    ["a", "b"],
                    ["c", "b"],
                    ["a", "b", "x"],
                    ["a", "b", "x", "y"],
                    ["w"],
                    ["w", "y"],
                ],
            ),
            [
                ["a"],
                ["a", "b"],
                ["c"],
                ["c", "b"],
            ],
        )
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().deleteDuplicateFolder(*args) == expected
