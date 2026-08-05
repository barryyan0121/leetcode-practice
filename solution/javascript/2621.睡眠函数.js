/** 2621. 睡眠函数 */
var sleep = function (millis) {
  return new Promise((resolve) => setTimeout(resolve, millis));
};
