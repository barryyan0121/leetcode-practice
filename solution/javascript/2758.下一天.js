/** 2758. 下一天 */
Date.prototype.nextDay = function () {
  const next = new Date(this);
  next.setDate(next.getDate() + 1);
  return next.toISOString().slice(0, 10);
};
