/** 2675. 将对象数组转换为矩阵 */
var jsonToMatrix = function (arr) {
  const flatten = (value, path, result) => {
    if (value !== null && typeof value === "object") {
      for (const [key, child] of Object.entries(value)) flatten(child, path.concat(key), result);
    } else result[path.join(".")] = value;
  };
  const rows = arr.map((object) => {
    const result = {};
    flatten(object, [], result);
    return result;
  });
  const columns = [...new Set(rows.flatMap((row) => Object.keys(row)))].sort();
  return [columns, ...rows.map((row) => columns.map((column) => (column in row ? row[column] : "")))];
};
