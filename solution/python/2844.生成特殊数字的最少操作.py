"""2844. 生成特殊数字的最少操作"""


class Solution:
    def minimumOperations(self, num: str) -> int:
        answer = len(num)
        for first, second in ("00", "25", "50", "75"):
            index = len(num) - 1
            while index >= 0 and num[index] != second:
                index -= 1
            if index < 0:
                continue
            index -= 1
            while index >= 0 and num[index] != first:
                index -= 1
            if index >= 0:
                answer = min(answer, len(num) - index - 2)
        return min(answer, len(num) - 1 if "0" in num else len(num))


if __name__ == "__main__":
    assert Solution().minimumOperations("2245047") == 2
    assert Solution().minimumOperations("2908305") == 3
    assert Solution().minimumOperations("10") == 1
    assert Solution().minimumOperations("1") == 1
