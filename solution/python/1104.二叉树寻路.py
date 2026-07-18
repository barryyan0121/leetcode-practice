class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        path = []
        level = label.bit_length() - 1
        while label:
            path.append(label)
            label = ((1 << level) + (1 << (level + 1)) - 1 - label) // 2
            level -= 1
        return path[::-1]


if __name__ == "__main__":
    test_cases = [
        (14, [1, 3, 4, 14]),
        (26, [1, 2, 6, 10, 26]),
        (1, [1]),
        (2, [1, 2]),
        (3, [1, 3]),
        (4, [1, 3, 4]),
    ]
    for _, (label, expected) in enumerate(test_cases):
        assert Solution().pathInZigZagTree(label) == expected
