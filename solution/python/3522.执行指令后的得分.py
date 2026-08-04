"""3522. 执行指令后的得分"""


class Solution:
    def calculateScore(self, instructions: list[str], values: list[int]) -> int:
        score = 0
        index = 0
        visited = set()
        while 0 <= index < len(instructions) and index not in visited:
            visited.add(index)
            if instructions[index] == "add":
                score += values[index]
                index += 1
            else:
                index += values[index]
        return score


if __name__ == "__main__":
    test_cases = [
        ((["jump", "add", "add", "jump", "add", "jump"], [2, 1, 3, 1, -2, -3]), 1),
        ((["jump", "add", "add"], [3, 1, 1]), 0),
        ((["jump"], [0]), 0),
    ]
    for _, ((instructions, values), expected) in enumerate(test_cases):
        assert Solution().calculateScore(instructions, values) == expected
