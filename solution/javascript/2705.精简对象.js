/** 2705. 精简对象 */
var compactObject = function (obj) {
  if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
  if (obj && typeof obj === "object") {
    return Object.fromEntries(Object.entries(obj).filter(([, value]) => Boolean(value)).map(([key, value]) => [key, compactObject(value)]));
  }
  return obj;
};
