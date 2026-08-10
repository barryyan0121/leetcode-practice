"""2213. 由单个字符重复的最长子字符串"""


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        size = 1
        while size < len(s):
            size <<= 1
        tree = [("", "", 0, 0, 0, 0)] * (size * 2)

        def merge(left, right):
            if not left[5]:
                return right
            if not right[5]:
                return left
            joined = left[1] == right[0]
            return (
                left[0],
                right[1],
                left[2] + right[2] if left[2] == left[5] and joined else left[2],
                right[3] + left[3] if right[3] == right[5] and joined else right[3],
                max(left[4], right[4], left[3] + right[2] if joined else 0),
                left[5] + right[5],
            )

        for i, char in enumerate(s):
            tree[size + i] = (char, char, 1, 1, 1, 1)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        answer = []
        for char, index in zip(queryCharacters, queryIndices):
            node = size + index
            tree[node] = (char, char, 1, 1, 1, 1)
            node //= 2
            while node:
                tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
                node //= 2
            answer.append(tree[1][4])
        return answer


if __name__ == "__main__":
    assert Solution().longestRepeating("babacc", "bcb", [1, 3, 3]) == [3, 3, 4]
