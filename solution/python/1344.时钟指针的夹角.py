# @lc app=leetcode.cn id=1344 lang=python3


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minute_angle = minutes * 6
        return min(abs(hour_angle - minute_angle), 360 - abs(hour_angle - minute_angle))


if __name__ == "__main__":
    test_cases = [
        (Solution().angleClock, (12, 30), 165.0),
        (Solution().angleClock, (3, 30), 75.0),
        (Solution().angleClock, (3, 15), 7.5),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1344 题 "时钟指针的夹角" 所有测试用例通过')
