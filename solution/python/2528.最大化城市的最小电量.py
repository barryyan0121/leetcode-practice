"""2528. 最大化城市的最小电量"""


class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0]
        for value in stations:
            prefix.append(prefix[-1] + value)
        power = [prefix[min(n, i + r + 1)] - prefix[max(0, i - r)] for i in range(n)]
        low, high = 0, sum(stations) + k + 1
        while low + 1 < high:
            target = (low + high) // 2
            extra = 0
            window = 0
            diff = [0] * (n + 1)
            possible = True
            for i in range(n):
                window += diff[i]
                need = target - power[i] - window
                if need > 0:
                    extra += need
                    if extra > k:
                        possible = False
                        break
                    window += need
                    diff[min(n, i + 2 * r + 1)] -= need
            if possible:
                low = target
            else:
                high = target
        return low


if __name__ == "__main__":
    test_cases = [(([1, 2, 4, 5, 0], 1, 2), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxPower(*args) == expected
