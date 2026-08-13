"""2381. 字母移位 II"""


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            change = 1 if direction else -1
            diff[start] += change
            diff[end + 1] -= change
        answer = []
        current = 0
        for index, char in enumerate(s):
            current += diff[index]
            answer.append(chr((ord(char) - ord("a") + current) % 26 + ord("a")))
        return "".join(answer)


if __name__ == "__main__":
    assert Solution().shiftingLetters("abc", [[0, 1, 0], [1, 2, 1]]) == "zbd"
