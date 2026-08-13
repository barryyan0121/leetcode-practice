"""2365. 任务调度器 II"""


class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        last = {}
        day = 0
        for task in tasks:
            if task in last:
                day = max(day, last[task] + space + 1)
            last[task] = day
            day += 1
        return day

if __name__ == "__main__":
    assert Solution().taskSchedulerII([1,2,1,2,3,1], 2) == 7
