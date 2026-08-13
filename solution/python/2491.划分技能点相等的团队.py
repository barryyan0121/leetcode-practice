"""2491. 划分技能点相等的团队"""


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        if any(
            skill[index] + skill[-index - 1] != target
            for index in range(len(skill) // 2)
        ):
            return -1
        return sum(skill[index] * skill[-index - 1] for index in range(len(skill) // 2))

if __name__ == "__main__":
    assert Solution().dividePlayers([3,2,5,1,3,4]) == 22
