"""2564. 子字符串异或查询"""


class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        positions = {}
        for start in range(len(s)):
            if s[start] == "0":
                positions.setdefault(0, [start, start])
                continue
            value = 0
            for end in range(start, min(len(s), start + 30)):
                value = value * 2 + int(s[end])
                positions.setdefault(value, [start, end])
        return [positions.get(a ^ b, [-1, -1]) for a, b in queries]


if __name__ == "__main__":
    test_cases = [(("101101", [[0, 5], [1, 2]]), [[0, 2], [2, 3]])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().substringXorQueries(*args) == expected
