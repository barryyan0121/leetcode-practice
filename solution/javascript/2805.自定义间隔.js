/** 2805. 自定义间隔 */
const activeIntervals = new Set();
let nextIntervalId = 0;

function customInterval(fn, delay, period) {
  const id = nextIntervalId++;
  activeIntervals.add(id);
  const run = (count) => {
    setTimeout(() => {
      if (!activeIntervals.has(id)) return;
      fn();
      run(count + 1);
    }, delay + count * period);
  };
  run(0);
  return id;
}

function customClearInterval(id) {
  activeIntervals.delete(id);
}
