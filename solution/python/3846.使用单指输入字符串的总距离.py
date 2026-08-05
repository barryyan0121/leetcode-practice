"""3846. 使用单指输入字符串的总距离"""


class Solution:
    def totalDistance(self, s: str) -> int:
        keyboard = "qwertyuiopasdfghjkl zxcvbnm"
        positions = {
            char: divmod(index, 10)
            for index, char in enumerate(keyboard)
            if char != " "
        }
        previous = positions["a"]
        answer = 0
        for char in s:
            current = positions[char]
            answer += abs(previous[0] - current[0]) + abs(previous[1] - current[1])
            previous = current
        return answer


if __name__ == "__main__":
    test_cases = [(("hello",), 17), (("a",), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().totalDistance(*args) == expected
