class Solution:
    def smallestSufficientTeam(
        self, req_skills: list[str], people: list[list[str]]
    ) -> list[int]:
        bit = {skill: index for index, skill in enumerate(req_skills)}
        dp = {0: []}
        for index, skills in enumerate(people):
            mask = 0
            for skill in skills:
                mask |= 1 << bit[skill]
            for covered, team in list(dp.items()):
                new_covered = covered | mask
                candidate = team + [index]
                if new_covered not in dp or len(candidate) < len(dp[new_covered]):
                    dp[new_covered] = candidate
        return dp[(1 << len(req_skills)) - 1]


if __name__ == "__main__":
    test_cases = [
        (
            ["java", "nodejs", "reactjs"],
            [["java"], ["nodejs"], ["nodejs", "reactjs"]],
            2,
        )
    ]
    for _, (req_skills, people, expected_length) in enumerate(test_cases):
        assert (
            len(Solution().smallestSufficientTeam(req_skills, people))
            == expected_length
        )
