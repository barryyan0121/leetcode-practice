"""2647. 把三角形染成红色"""


class Solution:
    def colorRed(self, n: int) -> list[list[int]]:
        answer = [[1, 1]]
        phase = 0
        for row in range(n, 1, -1):
            if phase == 0:
                for column in range(1, row * 2, 2):
                    answer.append([row, column])
            elif phase == 1:
                answer.append([row, 2])
            elif phase == 2:
                for column in range(3, row * 2, 2):
                    answer.append([row, column])
            else:
                answer.append([row, 1])
            phase = (phase + 1) % 4
        return answer


if __name__ == "__main__":
    test_cases = [((2,), [[1, 1], [2, 1], [2, 3]])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().colorRed(*args) == expected
