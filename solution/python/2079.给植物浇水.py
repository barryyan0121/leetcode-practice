"""2079. 给植物浇水"""


class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        water = capacity
        steps = 0
        for index, need in enumerate(plants):
            if water < need:
                steps += index * 2
                water = capacity
            water -= need
            steps += 1
        return steps


if __name__ == "__main__":
    test_cases = [(([2, 2, 3, 3], 5), 14)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().wateringPlants(*args) == expected
