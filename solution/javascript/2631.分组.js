/** 2631. 分组 */
Array.prototype.groupBy = function (fn) {
  return this.reduce((groups, value) => {
    const key = fn(value);
    (groups[key] ??= []).push(value);
    return groups;
  }, {});
};
