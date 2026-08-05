"""1989. 捉迷藏中可捕获的最大人数"""


class Solution:
    def catchMaximumAmountofPeople(self, team: list[int], dist: int) -> int:
        ghosts = [i for i, value in enumerate(team) if value == 1]
        people = [i for i, value in enumerate(team) if value == 0]
        ghost = person = answer = 0
        while ghost < len(ghosts) and person < len(people):
            if abs(ghosts[ghost] - people[person]) <= dist:
                answer += 1
                ghost += 1
                person += 1
            elif ghosts[ghost] < people[person]:
                ghost += 1
            else:
                person += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([0, 1, 0, 1, 0], 3), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().catchMaximumAmountofPeople(*args) == expected
