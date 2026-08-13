"""2880. 数据选取"""

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]


if __name__ == "__main__":
    students = pd.DataFrame(
        {
            "student_id": [101, 53, 128],
            "name": ["Ulysses", "William", "Henry"],
            "age": [13, 10, 6],
        }
    )
    expected = pd.DataFrame({"name": ["Ulysses"], "age": [13]}, index=[0])
    assert selectData(students).equals(expected)
    print("测试用例通过")
