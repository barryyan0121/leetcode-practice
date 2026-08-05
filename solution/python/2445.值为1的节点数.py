"""2445. 值为 1 的节点数"""


class Solution:
    def numberOfNodes(self, n: int, queries: list[int]) -> int:
        flips = [0] * (n + 1)
        for node in queries:
            flips[node] ^= 1
        answer = 0
        for node in range(1, n + 1):
            flips[node] ^= flips[node // 2]
            answer += flips[node]
        return answer


if __name__ == "__main__":
    test_cases = [((5, [1, 2, 5]), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfNodes(*args) == expected
