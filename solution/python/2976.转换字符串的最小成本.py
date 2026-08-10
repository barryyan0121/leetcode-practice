"""2976. 转换字符串的最小成本"""


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        infinity = 10**18
        distance = [[infinity] * 26 for _ in range(26)]
        for index in range(26):
            distance[index][index] = 0
        for left, right, value in zip(original, changed, cost):
            a, b = ord(left) - 97, ord(right) - 97
            distance[a][b] = min(distance[a][b], value)
        for middle in range(26):
            for left in range(26):
                for right in range(26):
                    distance[left][right] = min(
                        distance[left][right],
                        distance[left][middle] + distance[middle][right],
                    )
        answer = 0
        for left, right in zip(source, target):
            if left != right:
                value = distance[ord(left) - 97][ord(right) - 97]
                if value == infinity:
                    return -1
                answer += value
        return answer


if __name__ == "__main__":
    assert (
        Solution().minimumCost(
            "abcd",
            "acbe",
            ["a", "b", "c", "c", "e", "d"],
            ["b", "c", "b", "e", "b", "e"],
            [2, 5, 5, 1, 2, 20],
        )
        == 28
    )
