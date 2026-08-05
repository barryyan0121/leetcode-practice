var dateRangeGenerator = function* (start, end, step) {
  let date = new Date(`${start}T00:00:00Z`);
  const last = new Date(`${end}T00:00:00Z`);
  while (date <= last) {
    yield date.toISOString().slice(0, 10);
    date = new Date(date.getTime() + step * 86400000);
  }
};
