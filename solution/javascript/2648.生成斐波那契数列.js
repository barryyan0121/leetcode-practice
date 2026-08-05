/** 2648. 生成斐波那契数列 */
var fibGenerator = function* () {
  let first = 0;
  let second = 1;
  while (true) {
    yield first;
    [first, second] = [second, first + second];
  }
};
