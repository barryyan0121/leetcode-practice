"""2169. 得到 0 的操作数"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        answer = 0
        while num1 and num2:
            if num1 < num2:
                num1, num2 = num2, num1
            num1 -= num2
            answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [((2, 3), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countOperations(*args) == expected
