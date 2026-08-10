"""2844. 生成特殊数字的最少操作"""


class Solution:
    def minimumOperations(self, num: str) -> int:
        answer = len(num)
        for target in ("00", "25", "50", "75"):
            index = len(num) - 1
            deletions = 0
            for digit in reversed(target):
                while index >= 0 and num[index] != digit:
                    index -= 1
                    deletions += 1
                if index < 0:
                    break
                index -= 1
            else:
                answer = min(answer, deletions)
        return answer


if __name__ == "__main__":
    assert Solution().minimumOperations("2245047") == 2
