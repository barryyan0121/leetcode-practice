/** 2693. 使用自定义上下文调用函数 */
Function.prototype.callPolyfill = function (context, ...args) {
  const key = Symbol();
  context[key] = this;
  const result = context[key](...args);
  delete context[key];
  return result;
};
