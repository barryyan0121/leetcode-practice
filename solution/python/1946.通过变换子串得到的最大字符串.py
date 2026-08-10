"""1946. 通过变换子串得到的最大字符串"""


class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        result = list(num)
        changed = False
        for index, char in enumerate(result):
            replacement = str(change[int(char)])
            if changed and replacement < char:
                break
            if replacement > char:
                result[index] = replacement
                changed = True
        return "".join(result)


if __name__ == "__main__":
    assert Solution().maximumNumber("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == "832"
