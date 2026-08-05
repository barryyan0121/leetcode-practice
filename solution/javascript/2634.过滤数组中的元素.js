/** 2634. 过滤数组中的元素 */
var filter = function (arr, fn) {
  const answer = [];
  arr.forEach((value, index) => {
    if (fn(value, index)) answer.push(value);
  });
  return answer;
};
