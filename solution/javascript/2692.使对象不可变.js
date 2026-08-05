/** 2692. 使对象不可变 */
var makeImmutable = function (obj) {
  const methods = new Set(["pop", "push", "shift", "unshift", "splice", "sort", "reverse"]);
  return new Proxy(obj, {
    get(target, key) {
      if (Array.isArray(target) && methods.has(key)) throw `Error Calling Method: ${key}`;
      const value = target[key];
      return value && typeof value === "object" ? makeImmutable(value) : value;
    },
    set(target, key) {
      throw `${Array.isArray(target) ? "Error Modifying Index" : "Error Modifying"}: ${key}`;
    },
  });
};
