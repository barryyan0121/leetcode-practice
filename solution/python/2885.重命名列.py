import pandas as pd
from pandas.testing import assert_frame_equal


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )


class Solution:
    def renameColumns(self, students: pd.DataFrame) -> pd.DataFrame:
        return renameColumns(students)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {
                    "id": [1, 2],
                    "first": ["Ada", "Grace"],
                    "last": ["Lovelace", "Hopper"],
                    "age": [20, 25],
                }
            ),
            pd.DataFrame(
                {
                    "student_id": [1, 2],
                    "first_name": ["Ada", "Grace"],
                    "last_name": ["Lovelace", "Hopper"],
                    "age_in_years": [20, 25],
                }
            ),
        )
    ]

    solver = Solution()
    for index, (students, expected) in enumerate(test_cases):
        actual = solver.renameColumns(students.copy())
        assert_frame_equal(actual, expected), f"case {index} failed"
