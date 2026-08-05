from collections import Counter


class Solution:
    def minEliminationTime(self, timeReq: list[int], splitTime: int) -> int:
        counts = Counter(timeReq)
        n = len(timeReq)
        low, high = max(timeReq), max(timeReq) + splitTime * n.bit_length()

        def feasible(limit: int) -> bool:
            depths = []
            for duration, count in counts.items():
                if duration > limit:
                    return False
                depths.extend([(limit - duration) // splitTime] * count)
            depths.sort()
            slots = 1
            previous = 0
            for depth in depths:
                if slots == 0:
                    return False
                gap = depth - previous
                if gap >= n.bit_length():
                    slots = n
                else:
                    slots = min(n, slots << gap)
                slots -= 1
                previous = depth
            return True

        while low < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [
        (([10, 4, 5], 2), 12),
        (([10, 4], 5), 15),
    ]
    for _, ((time_req, split_time), expected) in enumerate(test_cases):
        assert Solution().minEliminationTime(time_req, split_time) == expected
