"""2657. 找到两个数组的前缀公共数组"""


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        first, second = set(), set()
        answer = []
        common = 0
        for x, y in zip(A, B):
            if x in second:
                common += 1
            if y in first:
                common += 1
            first.add(x)
            second.add(y)
            if x == y:
                common += 1
            answer.append(common)
        return answer


if __name__ == "__main__":
    assert Solution().findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]) == [
        0,
        2,
        3,
        4,
    ]
