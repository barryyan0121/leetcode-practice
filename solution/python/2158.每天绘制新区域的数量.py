"""2158. 每天绘制新区域的数量"""


class Solution:
    def amountPainted(self, paint: list[list[int]]) -> list[int]:
        next_unpainted = list(range(50002))

        def find(x: int) -> int:
            if next_unpainted[x] != x:
                next_unpainted[x] = find(next_unpainted[x])
            return next_unpainted[x]

        answer = []
        for start, end in paint:
            painted = 0
            position = find(start)
            while position < end:
                painted += 1
                next_unpainted[position] = find(position + 1)
                position = next_unpainted[position]
            answer.append(painted)
        return answer


if __name__ == "__main__":
    test_cases = [(([[1, 4], [4, 7], [5, 8]],), [3, 3, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().amountPainted(*args) == expected
