/** 2676. 节流 */
var throttle = function (fn, t) {
  let timer = null;
  let pending = null;
  const run = () => {
    if (pending) {
      const args = pending;
      pending = null;
      fn(...args);
      timer = setTimeout(run, t);
    } else timer = null;
  };
  return function (...args) {
    if (timer) pending = args;
    else {
      fn(...args);
      timer = setTimeout(run, t);
    }
  };
};
