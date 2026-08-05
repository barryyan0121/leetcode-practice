/** 2691. 不可变辅助工具 */
var ImmutableHelper = function (obj) {
  this.obj = obj;
};
ImmutableHelper.prototype.produce = function (mutator) {
  const copy = JSON.parse(JSON.stringify(this.obj));
  mutator(copy);
  return copy;
};
