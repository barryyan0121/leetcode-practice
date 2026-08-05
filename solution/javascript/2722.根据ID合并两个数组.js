var join = function (arr1, arr2) {
  const map = new Map(arr1.map((x) => [x.id, x]));
  for (const x of arr2) map.set(x.id, { ...map.get(x.id), ...x });
  return [...map.values()].sort((a, b) => a.id - b.id);
};
