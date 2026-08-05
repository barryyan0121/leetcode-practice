"""2120. 执行所有后缀指令后机器人所在位置"""


class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        answer = []
        moves = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
        for start in range(len(s)):
            row, col = startPos
            count = 0
            for command in s[start:]:
                dr, dc = moves[command]
                row += dr
                col += dc
                if not (0 <= row < n and 0 <= col < n):
                    break
                count += 1
            answer.append(count)
        return answer


if __name__ == "__main__":
    test_cases = [((3, [0, 1], "RRDDLU"), [1, 5, 4, 3, 1, 0])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().executeInstructions(*args) == expected
