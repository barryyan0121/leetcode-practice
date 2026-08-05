var QueryBatcher = function (queryMultiple, t) {
  this.queryMultiple = queryMultiple;
  this.t = t;
  this.queue = [];
  this.timer = null;
};

QueryBatcher.prototype.run = function (items) {
  Promise.resolve(this.queryMultiple(items.map((item) => item.key)))
    .then((values) => values.forEach((value, i) => items[i].resolve(value)))
    .catch((error) => items.forEach((item) => item.reject(error)));
};

QueryBatcher.prototype.flush = function () {
  this.timer = null;
  if (!this.queue.length) return;
  const items = this.queue;
  this.queue = [];
  this.run(items);
  this.timer = setTimeout(() => this.flush(), this.t);
};

QueryBatcher.prototype.getValue = function (key) {
  return new Promise((resolve, reject) => {
    this.queue.push({ key, resolve, reject });
    if (!this.timer) {
      const first = this.queue.splice(0, 1);
      this.run(first);
      this.timer = setTimeout(() => this.flush(), this.t);
    }
  });
};
