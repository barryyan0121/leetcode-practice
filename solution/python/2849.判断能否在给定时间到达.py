"""2849. 判断能否在给定时间到达"""


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        distance = max(abs(fx - sx), abs(fy - sy))
        return distance <= t and (distance != 0 or t != 1)


if __name__ == "__main__":
    assert Solution().isReachableAtTime(1, 1, 3, 3, 2)
