Array.prototype.upperBound = function (target) {
  let left = 0;
  let right = this.length - 1;
  let ans = -1;
  while (left <= right) {
    const mid = (left + right) >> 1;
    if (this[mid] === target) {
      ans = mid;
      left = mid + 1;
    } else if (this[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return ans;
};
