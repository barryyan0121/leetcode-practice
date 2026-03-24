import fs from "node:fs";
import path from "node:path";
import { chromium } from "playwright";

const [, , manifestPath, resultsPath, statePath] = process.argv;
const headless = process.env.HEADLESS !== "false";

if (!manifestPath || !resultsPath || !statePath) {
  console.error(
    "Usage: node submit_manifest.mjs <manifestPath> <resultsPath> <statePath>"
  );
  process.exit(1);
}

const rootDir = "/home/yanhan/Desktop/leetcode";
const manifestAbs = path.resolve(rootDir, manifestPath);
const resultsAbs = path.resolve(rootDir, resultsPath);
const stateAbs = path.resolve(rootDir, statePath);

const entries = fs
  .readFileSync(manifestAbs, "utf8")
  .split(/\r?\n/)
  .map((line) => line.trim())
  .filter(Boolean)
  .map((line) => {
    const [problem, slug, file] = line.split("|");
    return { problem: Number(problem), slug, file };
  });

function extractSubmissionCode(filePath) {
  const abs = path.resolve(rootDir, filePath);
  const text = fs.readFileSync(abs, "utf8");
  const lines = text.split(/\r?\n/);
  const start = lines.findIndex((line) => line.includes("@lc code=start"));
  if (start === -1) {
    throw new Error(`Missing @lc code=start in ${filePath}`);
  }

  let end = lines.findIndex(
    (line, idx) => idx > start && line.startsWith('if __name__ == "__main__":')
  );
  if (end === -1) {
    end = lines.length;
  }

  const body = lines
    .slice(start + 1, end)
    .filter((line) => !line.includes("@lc code=end"));

  while (body.length && !body[body.length - 1].trim()) {
    body.pop();
  }
  while (body.length && body[body.length - 1].trim() === "pass") {
    body.pop();
  }
  while (body.length && !body[body.length - 1].trim()) {
    body.pop();
  }

  const prelude = ["from typing import *"];
  if (text.includes("from collections import Counter, defaultdict")) {
    prelude.push("from collections import Counter, defaultdict");
  }

  return `${prelude.join("\n")}\n\n${body.join("\n")}\n`;
}

function appendResult(result) {
  fs.appendFileSync(resultsAbs, `${JSON.stringify(result)}\n`, "utf8");
}

async function ensurePython3(page) {
  const codeTab = page.getByText("代码", { exact: true }).first();
  if (await codeTab.count()) {
    await codeTab.click().catch(() => {});
    await page.waitForTimeout(300);
  }

  const python3Button = page.getByRole("button", {
    name: "Python3",
    exact: true,
  });
  if (await python3Button.count()) {
    return;
  }

  const languageButton = page
    .locator("button")
    .filter({
      hasText:
        /^(Python3|Python|C\+\+|Java|JavaScript|TypeScript|C#|C|Go|Kotlin|Swift|Rust)$/,
    })
    .first();

  if (await languageButton.count()) {
    await languageButton.click();
  } else {
    const buttonTexts = await page
      .locator("button")
      .evaluateAll((buttons) =>
        buttons
          .map((button) => button.textContent?.trim())
          .filter(Boolean)
          .slice(0, 60)
      );
    console.log(`BUTTONS ${JSON.stringify(buttonTexts)}`);
  }

  await page.waitForTimeout(500);
  const option = page.getByText("Python3", { exact: true }).last();
  await option.click();
  await page.waitForTimeout(1200);
}

async function submitEntry(page, context, entry) {
  const url = `https://leetcode.cn/problems/${entry.slug}/`;
  const result = {
    problem: entry.problem,
    slug: entry.slug,
    file: entry.file,
    status: "unknown",
    page_url: url,
  };

  try {
    console.log(`START ${entry.problem} ${entry.slug}`);
    await page.goto(url, { waitUntil: "domcontentloaded" });
    await page.waitForTimeout(1800);
    console.log(`LOADED ${entry.problem} ${page.url()}`);

    result.page_url = page.url();
    if (page.url().includes("/accounts/login")) {
      result.status = "skipped";
      result.reason = "login_required";
      appendResult(result);
      return;
    }

    await page.getByRole("button", { name: "提交" }).waitFor({ timeout: 15000 });
    console.log(`READY ${entry.problem}`);
    await ensurePython3(page);
    console.log(`LANG ${entry.problem}`);

    const code = extractSubmissionCode(entry.file);
    await page.waitForFunction(
      () => globalThis.monaco?.editor?.getModels?.()?.length > 0,
      { timeout: 15000 }
    );
    await page.evaluate((value) => {
      const model = monaco.editor.getModels()[0];
      model.setValue(value);
    }, code);
    await page.waitForTimeout(1200);
    console.log(`CODE ${entry.problem}`);

    const beforeUrl = page.url();
    await page.getByRole("button", { name: "提交" }).click();
    console.log(`SUBMIT ${entry.problem}`);
    await Promise.race([
      page.waitForURL(
        (nextUrl) => {
          const asText = nextUrl.toString();
          return asText.includes("/submissions/") && asText !== beforeUrl;
        },
        { timeout: 65000 }
      ),
      page.waitForFunction(
        () => {
          const text = document.body?.innerText ?? "";
          return (
            text.includes("测试结果") ||
            text.includes("通过") ||
            text.includes("答案错误") ||
            text.includes("执行出错") ||
            text.includes("编译错误") ||
            text.includes("超出时间限制")
          );
        },
        { timeout: 65000 }
      ),
    ]);
    await page.waitForTimeout(4000);

    const text = await page.locator("body").innerText();
    result.page_url = page.url();
    if (text.includes("通过")) {
      result.status = "passed";
    } else if (text.includes("答案错误")) {
      result.status = "failed";
      result.reason = "wrong_answer";
    } else if (text.includes("执行出错")) {
      result.status = "failed";
      result.reason = "runtime_error";
    } else if (text.includes("编译错误")) {
      result.status = "failed";
      result.reason = "compile_error";
    } else if (text.includes("超出时间限制")) {
      result.status = "failed";
      result.reason = "time_limit_exceeded";
    } else {
      result.status = "unknown";
    }

    const runtime = text.match(/([0-9]+)\s*ms/);
    const memory = text.match(/([0-9]+(?:\.[0-9]+)?)\s*MB/);
    if (runtime) {
      result.runtime_ms = runtime[1];
    }
    if (memory) {
      result.memory_mb = memory[1];
    }
  } catch (error) {
    result.status = "error";
    result.reason = String(error);
    result.page_url = page.url();
  }

  appendResult(result);
  console.log(`RESULT ${JSON.stringify(result)}`);
  await context.storageState({ path: stateAbs });
}

async function main() {
  fs.writeFileSync(resultsAbs, "", "utf8");

  const browser = await chromium.launch({
    headless,
    executablePath: "/usr/bin/google-chrome",
  });

  const context = await browser.newContext({
    storageState: stateAbs,
    viewport: { width: 1400, height: 960 },
  });
  const page = await context.newPage();

  for (const entry of entries) {
    await submitEntry(page, context, entry);
  }

  await context.storageState({ path: stateAbs });
  await browser.close();
}

await main();
