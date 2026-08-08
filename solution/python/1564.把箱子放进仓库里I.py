class Solution:
    def maxBoxesInWarehouse(self, boxes: list[int], warehouse: list[int]) -> int:
        for index in range(1, len(warehouse)):
            warehouse[index] = min(warehouse[index], warehouse[index - 1])
        boxes.sort()
        count = 0
        for capacity in reversed(warehouse):
            if count < len(boxes) and boxes[count] <= capacity:
                count += 1
        return count


if __name__ == "__main__":
    test_cases = [
        ([4, 3, 4, 1], [5, 3, 3, 4, 1], 3),
        ([1, 2, 2, 3, 4], [3, 4, 1, 2], 3),
    ]
    for _, (boxes, warehouse, expected) in enumerate(test_cases):
        assert Solution().maxBoxesInWarehouse(boxes, warehouse) == expected
