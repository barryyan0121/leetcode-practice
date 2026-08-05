/** 2618. 检查是否是类的对象实例 */
var checkIfInstanceOf = function (obj, classFunction) {
  if (obj === null || obj === undefined || typeof classFunction !== "function") return false;
  while (Object.getPrototypeOf(obj)) {
    if (Object.getPrototypeOf(obj) === classFunction.prototype) return true;
    obj = Object.getPrototypeOf(obj);
  }
  return false;
};
