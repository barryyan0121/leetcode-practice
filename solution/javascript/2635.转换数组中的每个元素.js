/** 2635. 转换数组中的每个元素 */
var map = function (arr, fn) {
  const answer = [];
  arr.forEach((value, index) => answer.push(fn(value, index)));
  return answer;
};
