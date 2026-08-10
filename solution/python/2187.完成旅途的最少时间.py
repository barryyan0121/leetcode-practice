"""2187. 完成旅途的最少时间"""


class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        low, high = 1, min(time) * totalTrips
        while low < high:
            middle = (low + high) // 2
            if sum(middle // value for value in time) >= totalTrips:
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    assert Solution().minimumTime([1, 2, 3], 5) == 3
