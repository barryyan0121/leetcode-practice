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
