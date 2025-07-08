import os
import re
from datetime import datetime, timezone, timedelta


def parse_filename(filename):
    """解析文件名，提取题号和题目名"""
    # 匹配格式：数字.题目名.py
    match = re.match(r"^(\d+)\.(.+)\.py$", filename)
    if match:
        return {
            "id": int(match.group(1)),
            "title": match.group(2),
            "filename": filename.replace(" ", "%20"),  # 替换空格为 %20
        }
    return None


def generate_readme_table(solutions):
    """生成 Markdown 表格"""
    # 按题号排序
    solutions.sort(key=lambda x: x["id"])

    # 生成表格内容
    table = "| 题号 | 题目名称 | 解决方案文件 |\n"
    table += "|------|----------|-------------|\n"

    for sol in solutions:
        file_link = f"[{sol['filename']}](./solution/python/{sol['filename']})"
        table += f"| {sol['id']} | {sol['title']} | {file_link} |\n"

    return table


def main():
    # 获取所有 Python 解决方案文件
    solution_dir = "solution/python"
    if not os.path.exists(solution_dir):
        print(f"解决方案目录不存在: {solution_dir}")
        return

    # 解析所有有效的解决方案文件
    solutions = []
    for filename in os.listdir(solution_dir):
        if filename.endswith(".py"):
            solution_info = parse_filename(filename)
            if solution_info:
                solutions.append(solution_info)

    if not solutions:
        print("未找到有效的解决方案文件")
        return

    print(f"找到 {len(solutions)} 个解决方案")

    # 生成 README 内容
    readme_content = "# LeetCode 解决方案\n\n"
    readme_content += "> 本仓库包含 LeetCode 题目的 Python 解决方案\n\n"
    readme_content += "## 解决方案列表\n\n"
    readme_content += generate_readme_table(solutions)

    # 创建 UTC+8 时区
    utc_plus_8 = timezone(timedelta(hours=8))

    # 获取当前 UTC+8 时间
    beijing_time = datetime.now(utc_plus_8)

    # 格式化为字符串
    timestamp = beijing_time.strftime("%Y-%m-%d %H:%M:%S")

    readme_content += f"\n\n**最后更新**: {timestamp} (UTC+8)"

    # 写入 README
    with open("README.md", "w") as f:
        f.write(readme_content)

    print("README.md 已更新")


if __name__ == "__main__":
    main()
