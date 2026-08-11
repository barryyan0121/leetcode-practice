/** 2821. 延迟每个 Promise 对象的解析 */
var delayAll = function (functions, ms) {
  return functions.map(
    (fn) =>
      () =>
        new Promise((resolve, reject) =>
          setTimeout(() => fn().then(resolve, reject), ms),
        ),
  );
};
