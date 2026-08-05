/** 2626. 数组归约运算 */
var reduce = function (nums, fn, init) {
  let answer = init;
  for (const value of nums) answer = fn(answer, value);
  return answer;
};
