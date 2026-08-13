import pandas as pd
from pandas.testing import assert_frame_equal


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] *= 2
    return employees


class Solution:
    def modifySalaryColumn(self, employees: pd.DataFrame) -> pd.DataFrame:
        return modifySalaryColumn(employees)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {"name": ["Jack", "Piper", "Mia"], "salary": [19666, 74754, 62509]}
            ),
            pd.DataFrame(
                {"name": ["Jack", "Piper", "Mia"], "salary": [39332, 149508, 125018]}
            ),
        )
    ]

    solver = Solution()
    for index, (employees, expected) in enumerate(test_cases):
        actual = solver.modifySalaryColumn(employees.copy())
        assert_frame_equal(actual, expected), f"case {index} failed"
