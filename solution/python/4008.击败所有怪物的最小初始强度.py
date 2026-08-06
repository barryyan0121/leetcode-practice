class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        norvelithx = (monsters, boosts)
        difference = [0] * (len(monsters) + 1)
        for left, right, value in boosts:
            difference[left] += value
            difference[right + 1] -= value
        bonus = 0
        spent = 0
        answer = 0
        for monster, change in zip(monsters, difference):
            bonus += change
            if bonus < monster:
                answer = max(answer, spent + monster - bonus)
            spent += monster
        return max(0, answer)


if __name__ == "__main__":
    solution = Solution()
    assert solution.minInitialStrength([5, 10, 15], [[1, 1, 10]]) == 30
    assert solution.minInitialStrength([5, 10, 15], [[1, 2, 10], [1, 2, 5]]) == 5
