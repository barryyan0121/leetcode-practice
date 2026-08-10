"""1923. 最长公共子路径"""

from collections import Counter


class Solution:
    def longestCommonSubpath(self, n: int, paths: list[list[int]]) -> int:
        modulo = 2**64 + 1
        base = 133331
        longest = max(map(len, paths))
        powers = [1] * (longest + 1)
        for index in range(1, longest + 1):
            powers[index] = powers[index - 1] * base % modulo
        hashes = []
        for path in paths:
            prefix = [0]
            for value in path:
                prefix.append((prefix[-1] * base + value) % modulo)
            hashes.append(prefix)

        def possible(length: int) -> bool:
            counts = Counter()
            for prefix in hashes:
                seen = set()
                for right in range(length, len(prefix)):
                    value = (
                        prefix[right] - prefix[right - length] * powers[length]
                    ) % modulo
                    if value not in seen:
                        seen.add(value)
                        counts[value] += 1
            return max(counts.values(), default=0) == len(paths)

        left, right = 0, min(map(len, paths))
        while left < right:
            middle = (left + right + 1) // 2
            if possible(middle):
                left = middle
            else:
                right = middle - 1
        return left


if __name__ == "__main__":
    assert (
        Solution().longestCommonSubpath(
            5, [[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3]]
        )
        == 2
    )
