Function.prototype.bindPolyfill = function (obj) {
  const fn = this;
  return (...args) => fn.apply(obj, args);
};
