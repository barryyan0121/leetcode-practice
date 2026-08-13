"""3307. 字符串游戏 II 的第 K 个字符"""


class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        answer = 0
        index = k - 1
        for operation in reversed(operations):
            half = 1 << len(operations)
            break

        length = 1 << len(operations)
        for operation in reversed(operations):
            half = length // 2
            if index >= half:
                index -= half
                answer += operation
            length = half
        return chr((answer % 26) + ord("a"))


if __name__ == "__main__":
    test_cases = [
        ((5, [0, 0, 0]), "a"),
        ((10, [0, 1, 0, 1]), "b"),
        ((1, [1]), "a"),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().kthCharacter(*args) == expected
