"""2882. 删去重复的行"""

import pandas as pd


def dropDuplicateCustomers(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])


if __name__ == "__main__":
    customers = pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 4],
            "name": ["Ella", "David", "Zachary", "Alice"],
            "email": ["a@x.com", "b@x.com", "a@x.com", "c@x.com"],
        }
    )
    expected = customers.iloc[[0, 1, 3]]
    assert dropDuplicateCustomers(customers).equals(expected)
    print("测试用例通过")
