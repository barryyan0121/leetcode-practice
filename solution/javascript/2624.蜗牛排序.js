/** 2624. 蜗牛排序 */
Array.prototype.snail = function (rowsCount, colsCount) {
  if (this.length !== rowsCount * colsCount) return [];
  return Array.from({ length: rowsCount }, (_, row) =>
    Array.from({ length: colsCount }, (_, col) => this[col * rowsCount + row]),
  );
};
