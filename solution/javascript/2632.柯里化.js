/** 2632. 柯里化 */
var curry = function (fn) {
  const collect = (args) => (...next) => {
    const all = args.concat(next);
    return all.length >= fn.length ? fn(...all) : collect(all);
  };
  return collect([]);
};
