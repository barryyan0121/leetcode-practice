/** 2629. 复合函数 */
var compose = function (functions) {
  return function (x) {
    return functions.reduceRight((value, fn) => fn(value), x);
  };
};
