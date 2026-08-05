/** 2700. 两个对象之间的差异 */
var objDiff = function (obj1, obj2) {
  if (obj1 === obj2) return {};
  if (typeof obj1 !== "object" || obj1 === null || typeof obj2 !== "object" || obj2 === null) return [obj1, obj2];
  const result = {};
  for (const key of Object.keys(obj1)) {
    if (key in obj2) {
      const difference = objDiff(obj1[key], obj2[key]);
      if (Array.isArray(difference) || Object.keys(difference).length) result[key] = difference;
    }
  }
  return result;
};
