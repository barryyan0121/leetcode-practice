/** 2694. 事件发射器 */
var EventEmitter = function () {
  this.events = new Map();
};
EventEmitter.prototype.subscribe = function (eventName, callback) {
  if (!this.events.has(eventName)) this.events.set(eventName, []);
  const callbacks = this.events.get(eventName);
  callbacks.push(callback);
  return { unsubscribe: () => callbacks.splice(callbacks.indexOf(callback), 1) };
};
EventEmitter.prototype.emit = function (eventName, args = []) {
  return (this.events.get(eventName) || []).map((callback) => callback(...args));
};
