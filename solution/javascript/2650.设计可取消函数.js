/** 2650. 设计可取消函数 */
var cancellable = function (fn, args, t) {
  const timer = setTimeout(() => fn(...args), t);
  return () => clearTimeout(timer);
};
