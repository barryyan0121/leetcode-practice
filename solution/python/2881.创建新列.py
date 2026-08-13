import pandas as pd
from pandas.testing import assert_frame_equal


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees


class Solution:
    def createBonusColumn(self, employees: pd.DataFrame) -> pd.DataFrame:
        return createBonusColumn(employees)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame({"name": ["Piper", "Grace"], "salary": [4548, 28150]}),
            pd.DataFrame(
                {
                    "name": ["Piper", "Grace"],
                    "salary": [4548, 28150],
                    "bonus": [9096, 56300],
                }
            ),
        )
    ]

    solver = Solution()
    for index, (employees, expected) in enumerate(test_cases):
        actual = solver.createBonusColumn(employees.copy())
        assert_frame_equal(actual, expected), f"case {index} failed"
