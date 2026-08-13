"""2884. 修改列"""

import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] *= 2
    return employees


if __name__ == "__main__":
    employees = pd.DataFrame(
        {"name": ["Jack", "Piper", "Mia"], "salary": [19666, 74754, 62509]}
    )
    expected = pd.DataFrame(
        {"name": ["Jack", "Piper", "Mia"], "salary": [39332, 149508, 125018]}
    )
    assert modifySalaryColumn(employees).equals(expected)
    print("测试用例通过")
