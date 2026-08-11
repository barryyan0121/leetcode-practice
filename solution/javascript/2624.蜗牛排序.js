/** 2624. 蜗牛排序 */
Array.prototype.snail = function (rowsCount, colsCount) {
  if (this.length !== rowsCount * colsCount) return [];
  const result = Array.from({ length: rowsCount }, () => []);
  for (let i = 0; i < this.length; i++) {
    const col = Math.floor(i / rowsCount);
    const row = col % 2 ? rowsCount - 1 - (i % rowsCount) : i % rowsCount;
    result[row][col] = this[i];
  }
  return result;
};
