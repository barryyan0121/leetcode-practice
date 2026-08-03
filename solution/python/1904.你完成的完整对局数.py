# @lc app=leetcode.cn id=1904 lang=python3


class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        start = self._minutes(loginTime)
        finish = self._minutes(logoutTime)
        if finish < start:
            finish += 24 * 60
        start = (start + 14) // 15 * 15
        finish = finish // 15 * 15
        return max(0, (finish - start) // 15)

    @staticmethod
    def _minutes(time: str) -> int:
        hour, minute = map(int, time.split(":"))
        return hour * 60 + minute


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfRounds, ("12:01", "12:44"), 1),
        (solution.numberOfRounds, ("20:00", "06:00"), 40),
        (solution.numberOfRounds, ("00:00", "00:00"), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1904 题 "你完成的完整对局数" 所有测试用例通过')
