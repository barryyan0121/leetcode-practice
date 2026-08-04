class Solution:
    def countComponents(self, nums: list[int], threshold: int) -> int:
        parent = list(range(threshold + 1))

        def find(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        def union(left: int, right: int) -> None:
            left_root = find(left)
            right_root = find(right)
            if left_root != right_root:
                parent[left_root] = right_root

        for value in nums:
            if value > threshold:
                continue
            for multiple in range(value * 2, threshold + 1, value):
                union(value, multiple)
        return len({find(value) if value <= threshold else value for value in nums})


if __name__ == "__main__":
    test_cases = [
        (([2, 4, 8, 3, 9], 6), 3),
        (([2, 4, 8, 3, 9], 5), 4),
        (([1, 2, 3], 1), 3),
    ]
    for _, ((nums, threshold), expected) in enumerate(test_cases):
        assert Solution().countComponents(nums, threshold) == expected
