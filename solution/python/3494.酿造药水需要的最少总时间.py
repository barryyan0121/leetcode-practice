"""3494. 酿造药水需要的最少总时间"""


class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        kelborthanz = (skill, mana)
        finish = [0] * len(skill)
        for power in mana:
            now = finish[0]
            for i in range(1, len(skill)):
                candidate = now + skill[i - 1] * power
                now = finish[i] if finish[i] > candidate else candidate
            finish[-1] = now + skill[-1] * power
            for i in range(len(skill) - 2, -1, -1):
                finish[i] = finish[i + 1] - skill[i + 1] * power
        return finish[-1]


if __name__ == "__main__":
    test_cases = [
        (([1, 5, 2, 4], [5, 1, 4, 2]), 110),
        (([1, 1, 1], [1, 1, 1]), 5),
        (([1, 2, 3, 4], [1, 2]), 21),
    ]
    for _, ((skill, mana), expected) in enumerate(test_cases):
        assert Solution().minTime(skill, mana) == expected
