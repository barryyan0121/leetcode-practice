import pandas as pd
from pandas.testing import assert_frame_equal


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


class Solution:
    def selectFirstRows(self, employees: pd.DataFrame) -> pd.DataFrame:
        return selectFirstRows(employees)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame({"employee_id": [1, 2, 3, 4], "name": list("ABCD")}),
            pd.DataFrame({"employee_id": [1, 2, 3], "name": list("ABC")}),
        )
    ]

    solver = Solution()
    for index, (employees, expected) in enumerate(test_cases):
        actual = solver.selectFirstRows(employees)
        assert_frame_equal(actual, expected), f"case {index} failed"
