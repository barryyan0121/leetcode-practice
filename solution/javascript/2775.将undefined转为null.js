var undefinedToNull = function (obj) {
  if (Array.isArray(obj)) return obj.map(undefinedToNull);
  if (obj && typeof obj === "object") {
    return Object.fromEntries(Object.entries(obj).map(([key, value]) => [key, value === undefined ? null : undefinedToNull(value)]));
  }
  return obj === undefined ? null : obj;
};
