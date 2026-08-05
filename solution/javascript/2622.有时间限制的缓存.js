/** 2622. 有时间限制的缓存 */
var TimeLimitedCache = function () {
  this.cache = new Map();
};
TimeLimitedCache.prototype.set = function (key, value, duration) {
  const existed = this.cache.has(key) && this.cache.get(key).expires > Date.now();
  if (this.cache.has(key)) clearTimeout(this.cache.get(key).timer);
  const timer = setTimeout(() => this.cache.delete(key), duration);
  this.cache.set(key, { value, expires: Date.now() + duration, timer });
  return existed;
};
TimeLimitedCache.prototype.get = function (key) {
  const item = this.cache.get(key);
  return item && item.expires > Date.now() ? item.value : -1;
};
TimeLimitedCache.prototype.count = function () {
  return [...this.cache.values()].filter((item) => item.expires > Date.now()).length;
};
