/** 2666. 只允许一次函数调用 */
var once = function (fn) {
  let called = false;
  let result;
  return function (...args) {
    if (called) return undefined;
    called = true;
    result = fn(...args);
    return result;
  };
};
