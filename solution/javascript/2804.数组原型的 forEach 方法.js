/** 2804. 数组原型的 forEach 方法 */
Array.prototype.forEach = function (callback, context) {
  for (let index = 0; index < this.length; index += 1) {
    callback.call(context, this[index], index, this);
  }
};
