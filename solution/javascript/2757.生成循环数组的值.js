var cycleGenerator = function* (arr, startIndex) {
  let index = ((startIndex % arr.length) + arr.length) % arr.length;
  while (true) {
    const step = yield arr[index];
    index = (index + (step ?? 1)) % arr.length;
    if (index < 0) index += arr.length;
  }
};
