"""2375. 根据模式串构造最小数字"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        answer = []
        for number in range(1, len(pattern) + 2):
            stack.append(str(number))
            if number == len(pattern) + 1 or pattern[number - 1] == "I":
                while stack:
                    answer.append(stack.pop())
        return "".join(answer)

if __name__ == "__main__":
    assert Solution().smallestNumber("IIIDIDDD") == "123549876"
