var partial = function (fn, args) {
  return function (...restArgs) {
    let index = 0;
    const merged = args.map((value) => value === "_" ? restArgs[index++] : value);
    return fn(...merged, ...restArgs.slice(index));
  };
};
