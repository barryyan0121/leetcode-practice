/** 2633. 将对象转换为 JSON 字符串 */
var jsonStringify = function (object) {
  if (object === null) return "null";
  if (typeof object === "string") return `"${object.replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`;
  if (typeof object !== "object") return String(object);
  if (Array.isArray(object)) return `[${object.map(jsonStringify).join(",")}]`;
  return `{${Object.keys(object).map((key) => `"${key}":${jsonStringify(object[key])}`).join(",")}}`;
};
