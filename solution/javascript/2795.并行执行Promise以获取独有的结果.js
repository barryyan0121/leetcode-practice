var promiseAllSettled = function (functions) {
  return Promise.all(functions.map((fn) => Promise.resolve().then(fn).then(
    (value) => ({ status: "fulfilled", value }),
    (reason) => ({ status: "rejected", reason }),
  )));
};
