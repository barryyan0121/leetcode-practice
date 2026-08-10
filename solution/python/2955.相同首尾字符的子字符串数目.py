"""2955. 相同首尾字符的子字符串数目"""


class Solution:
    def sameEndSubstringCount(self, s: str, queries: list[list[int]]) -> list[int]:
        prefix = [[0] * 26]
        for char in s:
            row = prefix[-1][:]
            row[ord(char) - 97] += 1
            prefix.append(row)
        answer = []
        for left, right in queries:
            answer.append(
                sum(
                    (prefix[right + 1][index] - prefix[left][index])
                    * (prefix[right + 1][index] - prefix[left][index] + 1)
                    // 2
                    for index in range(26)
                )
            )
        return answer


if __name__ == "__main__":
    assert Solution().sameEndSubstringCount("abcaab", [[0, 3], [1, 5], [2, 5]]) == [
        5,
        7,
        5,
    ]
