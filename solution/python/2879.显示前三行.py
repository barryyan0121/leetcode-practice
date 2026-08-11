"""2879. 显示前三行"""

import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


if __name__ == "__main__":
    employees = pd.DataFrame({"employee_id": [1, 2, 3, 4], "name": list("ABCD")})
    assert selectFirstRows(employees).equals(employees.head(3))
    print("测试用例通过")
