"""2613. 美数对"""

from bisect import bisect_left, bisect_right

try:
    from sortedcontainers import SortedList
except ImportError:

    class SortedList(list):
        def add(self, value):
            from bisect import insort

            insort(self, value)

        def irange(self, minimum, maximum):
            return iter(self[bisect_left(self, minimum) : bisect_right(self, maximum)])


class Solution:
    def beautifulPair(self, nums1: list[int], nums2: list[int]) -> list[int]:
        points = sorted(
            (x + y, x - y, index) for index, (x, y) in enumerate(zip(nums1, nums2))
        )
        best_distance = 10**18
        best_pair = [len(points), len(points)]
        active = SortedList()
        left = 0
        for u, v, index in points:
            while left < len(points) and u - points[left][0] > best_distance:
                active.remove((points[left][1], points[left][0], points[left][2]))
                left += 1
            for old_v, old_u, old_index in active.irange(
                (v - best_distance, -(10**18), -1),
                (v + best_distance, 10**18, 10**18),
            ):
                distance = max(u - old_u, abs(v - old_v))
                pair = sorted((index, old_index))
                if (distance, pair) < (best_distance, best_pair):
                    best_distance, best_pair = distance, pair
            active.add((v, u, index))
        return best_pair


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4], [1, 2, 3, 4]), [0, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().beautifulPair(*args) == expected
