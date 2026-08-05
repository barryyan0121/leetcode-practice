"""2015. 每段建筑物的平均高度"""

from collections import defaultdict


class Solution:
    def averageHeightOfBuildings(self, buildings: list[list[int]]) -> list[list[int]]:
        events = defaultdict(lambda: [0, 0])
        for start, end, height in buildings:
            events[start][0] += height
            events[start][1] += 1
            events[end][0] -= height
            events[end][1] -= 1
        positions = sorted(events)
        answer = []
        height_sum = count = 0
        for left, right in zip(positions, positions[1:]):
            height_sum += events[left][0]
            count += events[left][1]
            if count:
                segment = [left, right, height_sum // count]
                if answer and answer[-1][1] == left and answer[-1][2] == segment[2]:
                    answer[-1][1] = right
                else:
                    answer.append(segment)
        return answer


if __name__ == "__main__":
    test_cases = [(([[1, 5, 2], [2, 4, 3]],), [[1, 5, 2]])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().averageHeightOfBuildings(*args) == expected
