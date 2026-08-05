/** 2625. 扁平化嵌套数组 */
var flat = function (arr, n) {
  if (!n) return arr;
  const answer = [];
  for (const value of arr) {
    if (Array.isArray(value)) answer.push(...flat(value, n - 1));
    else answer.push(value);
  }
  return answer;
};
