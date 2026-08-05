"""2076. 处理含限制条件的好友请求"""


class Solution:
    def friendRequests(
        self, n: int, restrictions: list[list[int]], requests: list[list[int]]
    ) -> list[bool]:
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        answer = []
        for x, y in requests:
            rx, ry = find(x), find(y)
            allowed = all(not ({find(a), find(b)} == {rx, ry}) for a, b in restrictions)
            answer.append(allowed)
            if allowed and rx != ry:
                parent[rx] = ry
        return answer


if __name__ == "__main__":
    test_cases = [((3, [[0, 1]], [[0, 2], [2, 1]]), [True, False])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().friendRequests(*args) == expected
