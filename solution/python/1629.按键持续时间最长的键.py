# @lc app=leetcode.cn id=1629 lang=python3


class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        best_duration = releaseTimes[0]
        answer = keysPressed[0]
        for index in range(1, len(releaseTimes)):
            duration = releaseTimes[index] - releaseTimes[index - 1]
            if duration > best_duration or (
                duration == best_duration and keysPressed[index] > answer
            ):
                best_duration, answer = duration, keysPressed[index]
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.slowestKey, ([9, 29, 49, 50], "cbcd"), "c"),
        (solution.slowestKey, ([12, 23, 36, 46, 62], "spuda"), "a"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1629 题 "按键持续时间最长的键" 所有测试用例通过')
