var promisify = function (fn) {
  return async function (...args) {
    return new Promise((resolve, reject) => fn((value, error) => (error ? reject(error) : resolve(value)), ...args));
  };
};
