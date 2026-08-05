/** 2665. 计数器 II */
var createCounter = function (init) {
  let current = init;
  return {
    increment: () => ++current,
    decrement: () => --current,
    reset: () => (current = init),
  };
};
