class Solution:
    def maxBoxesInWarehouse(self, boxes: list[int], warehouse: list[int]) -> int:
        left = warehouse[:]
        right = warehouse[:]
        for index in range(1, len(warehouse)):
            left[index] = min(left[index], left[index - 1])
            right[-index - 1] = min(right[-index - 1], right[-index])
        capacities = sorted(max(a, b) for a, b in zip(left, right))
        boxes.sort()
        count = position = 0
        while count < len(boxes) and position < len(capacities):
            if boxes[count] <= capacities[position]:
                count += 1
            position += 1
        return count


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3, 4], [3, 4, 1, 2], 4),
        ([3, 5, 5, 2], [2, 1, 3, 4, 5], 3),
    ]
    for _, (boxes, warehouse, expected) in enumerate(test_cases):
        assert Solution().maxBoxesInWarehouse(boxes, warehouse) == expected
