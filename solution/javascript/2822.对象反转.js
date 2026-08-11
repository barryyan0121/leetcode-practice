/** 2822. 对象反转 */
var invertObject = function (obj) {
  const inverted = Object.create(null);
  for (const key in obj) {
    const value = obj[key];
    if (!(value in inverted)) inverted[value] = key;
    else if (Array.isArray(inverted[value])) inverted[value].push(key);
    else inverted[value] = [inverted[value], key];
  }
  return inverted;
};
