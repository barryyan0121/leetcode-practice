function* factorial(n) {
  let value = 1;
  yield value;
  for (let i = 2; i <= n; i += 1) {
    value *= i;
    yield value;
  }
}
