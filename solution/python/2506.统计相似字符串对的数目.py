"""2506. 统计相似字符串对的数目"""


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        masks = [sum(1 << (ord(char) - 97) for char in set(word)) for word in words]
        return sum(
            first == second
            for i, first in enumerate(masks)
            for second in masks[i + 1 :]
        )


if __name__ == "__main__":
    test_cases = [((["aba", "aabb", "abcd", "bac", "aabc"],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().similarPairs(*args) == expected
