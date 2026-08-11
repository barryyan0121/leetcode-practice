/** 2690. 无穷方法对象 */
var createInfiniteObject = function () {
  return new Proxy(
    {},
    {
      get: (target, property) => () => property,
    },
  );
};
