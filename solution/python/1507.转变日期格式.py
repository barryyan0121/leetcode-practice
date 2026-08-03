# @lc app=leetcode.cn id=1507 lang=python3


class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        months = {
            name: index
            for index, name in enumerate(
                (
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ),
                1,
            )
        }
        return f"{year}-{months[month]:02d}-{int(day[:-2]):02d}"


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.reformatDate, ("20th Oct 2052",), "2052-10-20")]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1507 题 "转变日期格式" 所有测试用例通过')
