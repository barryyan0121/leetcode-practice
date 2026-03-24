#!/usr/bin/env bash
set -uo pipefail

ROOT_DIR="/home/yanhan/Desktop/leetcode"
PWCLI="/home/yanhan/.codex/skills/playwright/scripts/playwright_cli.sh"
SESSION="${PLAYWRIGHT_SESSION:-leetcode-submit}"
RESULTS_FILE="${RESULTS_FILE_PATH:-$ROOT_DIR/output/playwright/leetcode-submit/results_1_200.jsonl}"
STATE_FILE="${STATE_FILE_PATH:-$ROOT_DIR/output/playwright/leetcode-submit/leetcode_cn_auth_state.json}"
if [[ $# -ge 2 ]]; then
  RESULTS_FILE="$2"
fi

default_entries=(
  "1|two-sum|solution/python/1.两数之和.py"
  "2|add-two-numbers|solution/python/2.两数相加.py"
  "3|longest-substring-without-repeating-characters|solution/python/3.无重复字符的最长子串.py"
  "4|median-of-two-sorted-arrays|solution/python/4.寻找两个正序数组的中位数.py"
  "6|zigzag-conversion|solution/python/6.Z 字形变换.py"
  "8|string-to-integer-atoi|solution/python/8.字符串转换整数 (atoi).py"
  "9|palindrome-number|solution/python/9.回文数.py"
  "42|trapping-rain-water|solution/python/42.接雨水.py"
  "56|merge-intervals|solution/python/56.合并区间.py"
  "70|climbing-stairs|solution/python/70.爬楼梯.py"
  "75|sort-colors|solution/python/75.颜色分类.py"
  "76|minimum-window-substring|solution/python/76.最小覆盖子串.py"
  "93|restore-ip-addresses|solution/python/93.复原 IP 地址.py"
  "101|symmetric-tree|solution/python/101.对称二叉树.py"
  "120|triangle|solution/python/120.三角形最小路径和.py"
  "165|compare-version-numbers|solution/python/165.比较版本号.py"
  "166|fraction-to-recurring-decimal|solution/python/166.分数到小数.py"
  "200|number-of-islands|solution/python/200.岛屿数量.py"
)

entries=()
if [[ $# -ge 1 ]]; then
  mapfile -t entries < "$1"
else
  entries=("${default_entries[@]}")
fi

extract_submission_code() {
  local file="$1"
  python3 - "$file" <<'PY'
from pathlib import Path
import sys

file = Path(sys.argv[1])
lines = file.read_text(encoding="utf-8").splitlines()

start = next(i for i, line in enumerate(lines) if "@lc code=start" in line) + 1
try:
    end = next(i for i, line in enumerate(lines[start:], start) if line.startswith('if __name__ == "__main__":'))
except StopIteration:
    end = len(lines)

body = [line for line in lines[start:end] if "@lc code=end" not in line]
while body and not body[-1].strip():
    body.pop()
while body and body[-1].strip() == "pass":
    body.pop()
while body and not body[-1].strip():
    body.pop()

prelude = ["from typing import *"]
text = file.read_text(encoding="utf-8")
if "from collections import Counter, defaultdict" in text:
    prelude.append("from collections import Counter, defaultdict")
if "import heapq" in text:
    prelude.append("import heapq")
if "import math" in text:
    prelude.append("import math")
if "import bisect" in text:
    prelude.append("import bisect")

print("\n".join(prelude))
print()
print("\n".join(body))
PY
}

json_string() {
  python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))'
}

: > "$RESULTS_FILE"

bash "$PWCLI" --session "$SESSION" open about:blank --headed >/dev/null 2>&1 || true
if [[ -f "$STATE_FILE" ]]; then
  bash "$PWCLI" --session "$SESSION" state-load "$STATE_FILE" >/dev/null 2>&1 || true
fi

for entry in "${entries[@]}"; do
  IFS="|" read -r number slug file <<<"$entry"
  abs_file="$ROOT_DIR/$file"
  url="https://leetcode.cn/problems/$slug/"

  if [[ ! -f "$abs_file" ]]; then
    printf '{"problem":"%s","slug":"%s","status":"skipped","reason":"missing_local_file"}\n' "$number" "$slug" | tee -a "$RESULTS_FILE"
    continue
  fi

  code_json=$(extract_submission_code "$abs_file" | json_string)
  url_json=$(printf '%s' "$url" | json_string)
  slug_json=$(printf '%s' "$slug" | json_string)

  js=$(cat <<EOF
async page => {
  const problem = ${number};
  const slug = ${slug_json};
  const url = ${url_json};
  const code = ${code_json};

  const result = {
    problem,
    slug,
    status: 'unknown',
    page_url: url,
  };

  try {
    const workPage = await page.context().newPage();
    try {
      await workPage.goto(url, { waitUntil: 'domcontentloaded' });
      await workPage.waitForTimeout(1800);

      result.page_url = workPage.url();
      if (workPage.url().includes('/accounts/login')) {
        result.status = 'skipped';
        result.reason = 'login_required';
        return result;
      }

      const submitButton = workPage.getByRole('button', { name: '提交' });
      await submitButton.waitFor({ timeout: 15000 });

      const python3Button = workPage.getByRole('button', { name: 'Python3', exact: true });
      if (!(await python3Button.count())) {
        const languageNames = ['C++', 'Java', 'Python', 'JavaScript', 'TypeScript', 'C#', 'C', 'Go', 'Kotlin', 'Swift', 'Rust'];
        for (const name of languageNames) {
          const button = workPage.getByRole('button', { name, exact: true }).first();
          if (await button.count()) {
            await button.click();
            break;
          }
        }
        await workPage.waitForTimeout(500);
        const option = workPage.getByText('Python3', { exact: true }).last();
        if (await option.count()) {
          await option.click();
          await workPage.waitForTimeout(1200);
        }
      }

      await workPage.waitForFunction(() => globalThis.monaco?.editor?.getModels?.()?.length > 0, { timeout: 15000 });
      await workPage.evaluate(value => {
        const model = monaco.editor.getModels()[0];
        model.setValue(value);
      }, code);
      await workPage.waitForTimeout(1200);

      await workPage.bringToFront();
      await workPage.waitForTimeout(500);
      await submitButton.click({ force: true });
      await workPage.waitForURL(nextUrl => nextUrl.toString().includes('/submissions/'), { timeout: 180000 });
      await workPage.waitForTimeout(4000);

      const text = await workPage.locator('body').innerText();
      result.page_url = workPage.url();
      if (text.includes('通过')) {
        result.status = 'passed';
      } else if (text.includes('答案错误')) {
        result.status = 'failed';
        result.reason = 'wrong_answer';
      } else if (text.includes('执行出错')) {
        result.status = 'failed';
        result.reason = 'runtime_error';
      } else if (text.includes('编译错误')) {
        result.status = 'failed';
        result.reason = 'compile_error';
      } else if (text.includes('超出时间限制')) {
        result.status = 'failed';
        result.reason = 'time_limit_exceeded';
      } else {
        result.status = 'unknown';
      }

      const runtime = text.match(/([0-9]+)\\s*ms/);
      const memory = text.match(/([0-9]+(?:\\.[0-9]+)?)\\s*MB/);
      if (runtime) result.runtime_ms = runtime[1];
      if (memory) result.memory_mb = memory[1];

      return result;
    } finally {
      await workPage.close();
    }
  } catch (error) {
    result.status = 'error';
    result.reason = String(error);
    result.page_url = page.url();
    return result;
  }
}
EOF
)

  output=$(bash "$PWCLI" --session "$SESSION" run-code "$js" 2>&1)
  run_status=$?
  printf '%s\n' "$output"

  result_line=$(printf '%s\n' "$output" | awk '/^### Result$/{getline; print; exit}')
  if [[ -n "$result_line" ]]; then
    printf '%s\n' "$result_line" | tee -a "$RESULTS_FILE"
    bash "$PWCLI" --session "$SESSION" state-save "$STATE_FILE" >/dev/null 2>&1 || true
  else
    printf '{"problem":"%s","slug":"%s","status":"error","reason":"cli_failure","exit_code":"%s"}\n' "$number" "$slug" "$run_status" | tee -a "$RESULTS_FILE"
  fi
done
