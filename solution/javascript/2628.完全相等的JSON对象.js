/** 2628. 完全相等的 JSON 对象 */
var areDeeplyEqual = function (o1, o2) {
  if (o1 === o2) return true;
  if (typeof o1 !== "object" || o1 === null || typeof o2 !== "object" || o2 === null) return false;
  const keys1 = Object.keys(o1);
  const keys2 = Object.keys(o2);
  return keys1.length === keys2.length && keys1.every((key) => Object.hasOwn(o2, key) && areDeeplyEqual(o1[key], o2[key]));
};
