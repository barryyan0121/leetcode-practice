/** 2710. 移除字符串中的尾随零 */
var removeTrailingZeros = function (num) {
  return num.replace(/0+$/, "");
};
