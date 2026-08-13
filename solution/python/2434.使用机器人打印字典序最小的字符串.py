"""2434. 使用机器人打印字典序最小的字符串"""


class Solution:
    def robotWithString(self, s: str) -> str:
        suffix_min = ["z"] * (len(s) + 1)
        for index in range(len(s) - 1, -1, -1):
            suffix_min[index] = min(s[index], suffix_min[index + 1])
        stack = []
        answer = []
        for index, char in enumerate(s):
            stack.append(char)
            while stack and stack[-1] <= suffix_min[index + 1]:
                answer.append(stack.pop())
        while stack:
            answer.append(stack.pop())
        return "".join(answer)


if __name__ == "__main__":
    assert Solution().robotWithString("zza") == "azz"
