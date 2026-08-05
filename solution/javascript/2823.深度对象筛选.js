var deepFilter = function (obj, fn) {
  if (Array.isArray(obj)) {
    const result = obj.map((value) => deepFilter(value, fn)).filter((value) => value !== undefined);
    return result.length ? result : undefined;
  }
  if (obj && typeof obj === "object") {
    const result = {};
    for (const [key, value] of Object.entries(obj)) {
      const filtered = deepFilter(value, fn);
      if (filtered !== undefined) result[key] = filtered;
    }
    return Object.keys(result).length ? result : undefined;
  }
  return fn(obj) ? obj : undefined;
};
