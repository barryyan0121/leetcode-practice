"""1946. 子字符串突变后可能得到的最大整数"""


class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        chars = list(num)
        started = False
        for i, char in enumerate(chars):
            value = str(change[int(char)])
            if value > char:
                chars[i] = value
                started = True
            elif started:
                break
        return "".join(chars)


if __name__ == "__main__":
    test_cases = [(("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]), "832")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumNumber(*args) == expected
