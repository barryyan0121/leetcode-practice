/** 2619. 数组原型对象的最后一个元素 */
Array.prototype.last = function () {
  return this.length ? this[this.length - 1] : -1;
};
