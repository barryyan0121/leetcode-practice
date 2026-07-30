from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups, waiting = [], defaultdict(list)
        for person, size in enumerate(groupSizes):
            waiting[size].append(person)
            if len(waiting[size]) == size:
                groups.append(waiting.pop(size))
        return groups


if __name__ == "__main__":
    test_cases = [([3, 3, 3, 3, 3, 1, 3], [[0, 1, 2], [5], [3, 4, 6]])]
    for _, (sizes, expected) in enumerate(test_cases):
        assert Solution().groupThePeople(sizes) == expected
