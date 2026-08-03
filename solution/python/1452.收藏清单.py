# @lc app=leetcode.cn id=1452 lang=python3


class Solution:
    def peopleIndexes(self, favoriteCompanies: list[list[str]]) -> list[int]:
        sets = [set(companies) for companies in favoriteCompanies]
        return [
            index
            for index, companies in enumerate(sets)
            if not any(
                index != other_index and companies <= other
                for other_index, other in enumerate(sets)
            )
        ]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.peopleIndexes,
            (
                [
                    ["leetcode", "google", "facebook"],
                    ["google", "microsoft"],
                    ["google", "facebook"],
                    ["google"],
                ],
            ),
            [0, 1],
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1452 题 "收藏清单" 所有测试用例通过')
