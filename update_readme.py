import os
import re
from datetime import datetime


# 解析文件名获取题目信息
def parse_filename(filename):
    # 提取题号和标题
    match = re.search(r"solution/(\d+)-(.+?)\.(\w+)$", filename)
    if match:
        problem_id = match.group(1)
        slug = match.group(2).replace(" ", "-").lower()
        extension = match.group(3)
        title = match.group(2).replace("-", " ").title()

        # 生成 LeetCode 链接
        leetcode_link = f"https://leetcode.com/problems/{slug}/"

        # 获取语言名称
        lang_names = {
            "py": "Python",
            "java": "Java",
            "cpp": "C++",
            "c": "C",
            "js": "JavaScript",
            "ts": "TypeScript",
            "go": "Go",
            "rs": "Rust",
            "swift": "Swift",
            "rb": "Ruby",
            "kt": "Kotlin",
        }
        language = lang_names.get(extension, extension.upper())

        return {
            "id": problem_id,
            "title": title,
            "slug": slug,
            "language": language,
            "link": leetcode_link,
            "file_link": f"./{filename}",  # GitHub 上的相对链接
        }
    return None


# 主处理逻辑
def main():
    # 获取新增文件列表
    new_files = os.getenv("NEW_FILES", "").splitlines()
    new_solutions = []
    new_files = [
        "python/1353.最多可以参加的会议数目.py",
        "python/1394.找出数组中的幸运数.py",
        "python/1865.找出和为指定值的下标对.py",
    ]

    # 解析每个文件
    for file in new_files:
        solution = parse_filename(file)
        if solution:
            new_solutions.append(solution)

    if not new_solutions:
        print("No valid solutions found for README update")
        return

    # 按题号排序
    new_solutions.sort(key=lambda x: int(x["id"]))

    # 生成 Markdown 表格行
    table_rows = []
    for sol in new_solutions:
        row = f"| {sol['id']} | [{sol['title']}]({sol['link']}) | "
        row += f"[{sol['language']}]({sol['file_link']}) |"
        table_rows.append(row)

    # 读取现有的 README
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            content = f.read()
    else:
        content = "# LeetCode Solutions\n\n"
        content += "| ID | Title | Solution |\n"
        content += "|----|-------|----------|\n"

    # 检查表格是否存在，如果不存在则创建
    if "| ID | Title | Solution |" not in content:
        content += "\n\n## Solutions\n\n"
        content += "| ID | Title | Solution |\n"
        content += "|----|-------|----------|\n"

    # 在表格开头添加新行（按题号排序后）
    table_header = "| ID | Title | Solution |\n|----|-------|----------|"
    if table_header in content:
        # 在表格开头插入新行
        new_table = table_header + "\n" + "\n".join(table_rows) + "\n"
        content = content.replace(table_header, new_table, 1)
    else:
        # 如果找不到表格头，在文件末尾添加新表格
        content += "\n".join(table_rows) + "\n"

    # 添加更新时间
    update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content += f"\n\n> Last updated: {update_time} (UTC)"

    # 写入 README
    with open(readme_path, "w") as f:
        f.write(content)

    print(f"Added {len(new_solutions)} solutions to README")


if __name__ == "__main__":
    main()
