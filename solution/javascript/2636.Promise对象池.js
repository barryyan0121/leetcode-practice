/** 2636. Promise 对象池 */
var promisePool = async function (functions, n) {
  let next = 0;
  const worker = async () => {
    while (next < functions.length) await functions[next++]();
  };
  await Promise.all(Array.from({ length: Math.min(n, functions.length) }, worker));
};
