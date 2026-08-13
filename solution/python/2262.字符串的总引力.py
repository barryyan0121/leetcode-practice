"""2262. 字符串的总引力"""


class Solution:
    def appealSum(self, s: str) -> int:
        last = {}
        answer = current = 0
        for i, char in enumerate(s):
            current += i - last.get(char, -1)
            answer += current
            last[char] = i
        return answer


if __name__ == "__main__":
    assert Solution().appealSum("abbca") == 28
