#
# @lc app=leetcode.cn id=635 lang=python3
#
# [635] 设计日志存储系统
#


# @lc code=start
class LogSystem:
    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str):
        length = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }[granularity]
        start, end = start[:length], end[:length]
        return [
            id
            for id, timestamp in sorted(self.logs, key=lambda item: item[1])
            if start <= timestamp[:length] <= end
        ]


# @lc code=end


if __name__ == "__main__":
    system = LogSystem()
    system.put(1, "2017:01:01:23:59:59")
    system.put(2, "2017:01:02:23:59:59")
    assert system.retrieve("2017:01:01:00:00:00", "2017:01:02:23:59:59", "Day") == [
        1,
        2,
    ]
