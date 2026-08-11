/** 2649. 嵌套数组生成器 */
var inorderTraversal = function* (arr) {
  for (const value of arr) {
    if (Array.isArray(value)) yield* inorderTraversal(value);
    else yield value;
  }
};
