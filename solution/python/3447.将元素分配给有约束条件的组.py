class Solution:
    def assignElements(self, groups: list[int], elements: list[int]) -> list[int]:
        maximum = max(groups)
        assigned_by_value = {group: -1 for group in groups}
        seen = set()
        for index, element in enumerate(elements):
            if element in seen or element > maximum:
                continue
            seen.add(element)
            for multiple in range(element, maximum + 1, element):
                if multiple in assigned_by_value and assigned_by_value[multiple] == -1:
                    assigned_by_value[multiple] = index
        return [assigned_by_value[group] for group in groups]


if __name__ == "__main__":
    test_cases = [
        (([8, 4, 3, 2, 4], [4, 2]), [0, 0, -1, 1, 0]),
        (([2, 3, 5, 7], [5, 3, 3]), [-1, 1, 0, -1]),
        (([10, 21, 30, 41], [2, 1]), [0, 1, 0, 1]),
    ]
    for _, ((groups, elements), expected) in enumerate(test_cases):
        assert Solution().assignElements(groups, elements) == expected
