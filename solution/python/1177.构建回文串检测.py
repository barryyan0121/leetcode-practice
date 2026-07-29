from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for char in s:
            prefix.append(prefix[-1] ^ (1 << (ord(char) - ord("a"))))
        return [
            ((prefix[right + 1] ^ prefix[left]).bit_count() // 2 <= k)
            for left, right, k in queries
        ]


if __name__ == "__main__":
    test_cases = [
        (
            "abcda",
            [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2]],
            [True, False, False, True],
        )
    ]
    for _, (s, queries, expected) in enumerate(test_cases):
        assert Solution().canMakePaliQueries(s, queries) == expected
