/** 2650. 设计可取消函数 */
var cancellable = function (generator) {
  let resolve, reject, pending = false, token = 0;
  const promise = new Promise((a, b) => {
    resolve = a;
    reject = b;
  });
  const step = (value, throwing) => {
    let result;
    try {
      result = throwing ? generator.throw(value) : generator.next(value);
    } catch (error) {
      pending = false;
      reject(error);
      return;
    }
    if (result.done) {
      pending = false;
      resolve(result.value);
      return;
    }
    pending = true;
    const current = ++token;
    Promise.resolve(result.value).then(
      (value) => current === token && step(value, false),
      (error) => current === token && step(error, true),
    );
  };
  step();
  return [() => pending && (token++, step("Cancelled", true)), promise];
};
