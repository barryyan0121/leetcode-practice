/** 2704. 相等还是不相等 */
var expect = function (val) {
  return {
    toBe(other) {
      if (val !== other) throw new Error("Not Equal");
      return true;
    },
    notToBe(other) {
      if (val === other) throw new Error("Equal");
      return true;
    },
  };
};
