"""2410. 运动员和训练师的最大匹配数"""


class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        answer = 0
        for trainer in trainers:
            if answer < len(players) and players[answer] <= trainer:
                answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([4, 7, 9], [8, 2, 5, 8]), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().matchPlayersAndTrainers(*args) == expected
