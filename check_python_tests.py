import os
import sys


def check_test_files():
    """检查每个解决方案文件是否包含完整的测试结构"""
    solution_dir = "solution/python"
    errors = []
    test_patterns = [
        "test_cases",  # 测试用例列表
        "enumerate(test_cases)",  # 测试循环
        "assert",  # 断言语句
    ]

    # get rid of strings and then convert the rest to int
    dirs = sorted(
        os.listdir(solution_dir),
        key=lambda x: (
            int(x.split(".")[0].split(" ")[-1])
            if x.split(".")[0].split(" ")[-1].isdigit()
            else 0
        ),
    )

    for filename in dirs:
        if filename.endswith(".py"):
            filepath = os.path.join(solution_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

                # 检查是否存在主执行块
                if "if __name__" not in content:
                    errors.append(f"{filename} 缺少主执行块 (if __name__ == ...)")
                    continue

                # 检查测试结构关键元素
                missing_patterns = []
                for pattern in test_patterns:
                    if pattern not in content:
                        missing_patterns.append(pattern)

                if missing_patterns:
                    missing_str = ", ".join(missing_patterns)
                    errors.append(f"{filename} 缺少测试元素: {missing_str}")

    if errors:
        print("\n".join(errors))
        print(f"发现 {len(errors)} 个测试相关问题")
        return False
    return True


def main():
    if not check_test_files():
        sys.exit(1)
    print("所有解决方案文件均包含完整的测试结构")


if __name__ == "__main__":
    main()
