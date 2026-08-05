/** 2677. 分块数组 */
var chunk = function (arr, size) {
  const answer = [];
  for (let index = 0; index < arr.length; index += size) answer.push(arr.slice(index, index + size));
  return answer;
};
