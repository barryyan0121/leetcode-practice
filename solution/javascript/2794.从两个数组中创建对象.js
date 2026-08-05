var createObject = function (keysArr, valuesArr) {
  const result = {};
  keysArr.forEach((key, i) => {
    key = String(key);
    if (!Object.prototype.hasOwnProperty.call(result, key)) result[key] = valuesArr[i];
  });
  return result;
};
