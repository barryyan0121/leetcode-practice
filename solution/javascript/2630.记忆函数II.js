/** 2630. 记忆函数 II */
var memoize = function (fn) {
  const cache = new Map();
  return function (...args) {
    let node = cache;
    for (const arg of args) {
      if (!node.has(arg)) node.set(arg, new Map());
      node = node.get(arg);
    }
    if (!node.has("value")) node.set("value", fn(...args));
    return node.get("value");
  };
};
