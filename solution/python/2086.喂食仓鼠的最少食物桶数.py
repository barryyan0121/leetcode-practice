"""2086. 喂食仓鼠的最少食物桶数"""


class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        cells = list(hamsters)
        answer = 0
        for index, char in enumerate(cells):
            if char != "H":
                continue
            if index > 0 and cells[index - 1] == "B":
                continue
            if index + 1 < len(cells) and cells[index + 1] == ".":
                cells[index + 1] = "B"
                answer += 1
            elif index > 0 and cells[index - 1] == ".":
                cells[index - 1] = "B"
                answer += 1
            else:
                return -1
        return answer


if __name__ == "__main__":
    test_cases = [("H.H", 1), (("HHH",), -1)]
    for _, (args, expected) in enumerate(test_cases):
        args = (args,) if isinstance(args, str) else args
        assert Solution().minimumBuckets(*args) == expected
