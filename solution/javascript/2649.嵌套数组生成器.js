/** 2649. 嵌套数组生成器 */
var inOrder = function* (arr) {
  for (const value of arr) {
    if (Array.isArray(value)) yield* inOrder(value);
    else yield value;
  }
};
