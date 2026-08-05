"""3598. 相邻字符串之间的最长公共前缀"""


class Solution:
    def longestCommonPrefix(self, words: list[str]) -> list[int]:
        n = len(words)
        adjacent = [0] * max(n - 1, 0)
        for i in range(n - 1):
            while (
                adjacent[i] < min(len(words[i]), len(words[i + 1]))
                and words[i][adjacent[i]] == words[i + 1][adjacent[i]]
            ):
                adjacent[i] += 1
        prefix = [0] * n
        suffix = [0] * n
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], adjacent[i - 1])
            suffix[n - i - 1] = max(suffix[n - i], adjacent[n - i - 1])
        answer = []
        for i in range(n):
            bridge = 0
            if i and i + 1 < n:
                while (
                    bridge < min(len(words[i - 1]), len(words[i + 1]))
                    and words[i - 1][bridge] == words[i + 1][bridge]
                ):
                    bridge += 1
            answer.append(
                max(
                    prefix[i - 1] if i else 0, suffix[i + 1] if i + 1 < n else 0, bridge
                )
            )
        return answer


if __name__ == "__main__":
    test_cases = [
        ((["jump", "run", "run", "jump", "run"],), [3, 0, 0, 3, 3]),
        ((["abc", "bcd", "cde"],), [0, 0, 0]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().longestCommonPrefix(*args) == expected
