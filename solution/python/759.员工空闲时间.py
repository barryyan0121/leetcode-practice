#
# @lc app=leetcode.cn id=759 lang=python3
#
# [759] 员工空闲时间
#


# @lc code=start
class Solution:
    def employeeFreeTime(self, schedule):
        intervals = sorted(
            (interval for employee in schedule for interval in employee),
            key=lambda interval: interval.start,
        )
        result = []
        end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start > end:
                result.append(Interval(end, interval.start))
            end = max(end, interval.end)
        return result


# @lc code=end

if __name__ == "__main__":

    class Interval:
        def __init__(self, start, end):
            self.start, self.end = start, end

    result = Solution().employeeFreeTime(
        [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]
    )
    assert [(x.start, x.end) for x in result] == [(3, 4)]


if __name__ == "__main__":

    class Interval:
        def __init__(self, start, end):
            self.start, self.end = start, end

    schedule = [
        [Interval(1, 2), Interval(5, 6)],
        [Interval(1, 3)],
        [Interval(4, 10)],
    ]
    ans = Solution().employeeFreeTime(schedule)
    assert [(x.start, x.end) for x in ans] == [(3, 4)]
