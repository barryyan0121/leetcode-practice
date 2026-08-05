/** 2637. 有时间限制的 Promise 对象 */
var timeLimit = function (fn, t) {
  return function (...args) {
    return Promise.race([
      Promise.resolve().then(() => fn(...args)),
      new Promise((_, reject) => setTimeout(() => reject("Time Limit Exceeded"), t)),
    ]);
  };
};
