var deepMerge = function (obj1, obj2) {
  if (obj1 === null || obj2 === null || typeof obj1 !== "object" || typeof obj2 !== "object") return obj2;
  if (Array.isArray(obj1) !== Array.isArray(obj2)) return obj2;
  const result = Array.isArray(obj1) ? [...obj1] : { ...obj1 };
  for (const key of Object.keys(obj2)) result[key] = key in result ? deepMerge(result[key], obj2[key]) : obj2[key];
  return result;
};
