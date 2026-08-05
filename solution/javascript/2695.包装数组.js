/** 2695. 包装数组 */
var ArrayWrapper = function (nums) {
  this.nums = nums;
};
ArrayWrapper.prototype.valueOf = function () {
  return this.nums.reduce((sum, value) => sum + value, 0);
};
ArrayWrapper.prototype.toString = function () {
  return `[${this.nums.join(",")}]`;
};
