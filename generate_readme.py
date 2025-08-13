import os
import re
import ast
import subprocess
from datetime import datetime, timezone, timedelta


def parse_filename(filename):
    """解析文件名，提取题号和题目名"""
    # 匹配格式：数字.题目名.py
    match = re.match(r"^(\d+)\.(.+)\.py$", filename)
    if match:
        return {
            "id": int(match.group(1)),
            "title": match.group(2),
            "filename": filename,
        }
    return None


def get_last_modified_time(filepath):
    """
    获取文件的最后修改时间（优先使用 Git 历史记录）
    返回格式化的时间字符串 (UTC+8)
    """
    try:
        # 尝试使用 Git 获取最后提交时间
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cd", "--date=iso", "--", filepath],
            capture_output=True,
            text=True,
            check=True,
        )

        if result.stdout.strip():
            git_time_str = result.stdout.strip()
            # 解析 ISO 格式时间
            dt = datetime.strptime(git_time_str, "%Y-%m-%d %H:%M:%S %z")
            # 转换为 UTC+8
            dt_utc8 = dt.astimezone(timezone(timedelta(hours=8)))
            return dt_utc8.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(f"无法获取 {filepath} 的 Git 历史: {e}")

    try:
        # 如果 Git 不可用，使用文件系统修改时间
        mtime = os.path.getmtime(filepath)
        dt = datetime.fromtimestamp(mtime, timezone(timedelta(hours=8)))
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception as e:
        print(f"无法获取 {filepath} 的文件修改时间: {e}")
        return "未知时间"


def is_implemented(filepath):
    """检查解决方案是否已实现（非空函数体）"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 使用 AST 解析代码
        tree = ast.parse(content)

        # 查找 Solution 类
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # 查找类中的方法
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        # 检查函数体是否为空或只有 pass
                        if len(item.body) == 0:
                            return False
                        if len(item.body) == 1 and isinstance(item.body[0], ast.Pass):
                            return False
                        return True
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"解析 {filepath} 时出错: {e}")
    return False


def generate_readme_table(solutions, title):
    """生成 Markdown 表格"""
    if not solutions:
        return ""

    # 按题号排序
    solutions.sort(key=lambda x: x["id"])

    # 生成表格内容
    table = f"## {title}\n\n"
    table += "| 题号 | 题目名称 | 解决方案文件 | 最后修改时间 |\n"
    table += "|------|----------|--------------|-------------|\n"

    for sol in solutions:
        file_link = f"[Python](./solution/python/{sol['filename'].replace(' ', '%20')})"
        table += f"| {sol['id']} | {sol['title']} | {file_link} |  {sol['last_modified']} |\n"

    return table + "\n"


def main():
    # 获取所有 Python 解决方案文件
    solution_dir = "solution/python"
    if not os.path.exists(solution_dir):
        print(f"解决方案目录不存在: {solution_dir}")
        return

    # 解析所有有效的解决方案文件并检查是否实现
    completed_solutions = []
    todo_solutions = []

    # 解析所有有效的解决方案文件
    for filename in os.listdir(solution_dir):
        if filename.endswith(".py"):
            solution_info = parse_filename(filename)
            if solution_info:
                filepath = os.path.join(solution_dir, filename)
                # 获取最后修改时间
                solution_info["last_modified"] = get_last_modified_time(
                    filepath=filepath
                )
                if is_implemented(filepath):
                    completed_solutions.append(solution_info)
                else:
                    todo_solutions.append(solution_info)

    print(f"找到 {len(completed_solutions)} 个已完成的解决方案")
    print(f"找到 {len(todo_solutions)} 个待完成的解决方案")

    # 生成 README 内容
    readme_content = "# LeetCode 解决方案\n\n"
    readme_content += "> 本仓库包含 LeetCode 题目的 Python 解决方案\n\n"

    # 添加已完成的解决方案表格
    readme_content += generate_readme_table(completed_solutions, "已完成的题目")

    # 添加待完成的解决方案表格
    if todo_solutions:
        readme_content += generate_readme_table(todo_solutions, "待完成的题目")
        readme_content += "> 提示：这些题目的解决方案尚未完成，欢迎贡献代码！\n"

    # 创建 UTC+8 时区
    utc_plus_8 = timezone(timedelta(hours=8))
    timestamp = datetime.now(utc_plus_8).strftime("%Y-%m-%d %H:%M:%S")
    readme_content += f"**最后更新**: {timestamp} (UTC+8)\n"

    # 写入 README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README.md 已更新")


if __name__ == "__main__":
    main()
