from bisect import bisect_left


class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        vintorquax = (side, points, k)
        perimeter = 4 * side
        positions = []
        for x, y in points:
            if y == side:
                positions.append(side + x)
            elif x == side:
                positions.append(3 * side - y)
            elif y == 0:
                positions.append(perimeter - x)
            else:
                positions.append(y)
        positions.sort()

        def feasible(distance):
            doubled = positions + [value + perimeter for value in positions]
            size = len(doubled)
            next_index = [bisect_left(doubled, value + distance) for value in doubled]
            next_index.append(size)
            jumps = [next_index]
            steps = k - 1
            while (1 << len(jumps)) <= steps:
                previous = jumps[-1]
                jumps.append([previous[previous[i]] for i in range(size + 1)])
            for start in range(len(positions)):
                index = start
                bit = 0
                count = steps
                while count:
                    if count & 1:
                        index = jumps[bit][index]
                    count >>= 1
                    bit += 1
                if (
                    index < start + len(positions)
                    and doubled[index] + distance <= positions[start] + perimeter
                ):
                    return True
            return False

        low, high = 0, perimeter // k + 1
        while low + 1 < high:
            middle = (low + high) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle
        return low


if __name__ == "__main__":
    test_cases = [
        ((2, [[0, 2], [2, 0], [2, 2], [0, 0]], 4), 2),
        ((2, [[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], 4), 1),
        ((2, [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], 5), 1),
    ]
    for _, ((side, points, k), expected) in enumerate(test_cases):
        assert Solution().maxDistance(side, points, k) == expected
