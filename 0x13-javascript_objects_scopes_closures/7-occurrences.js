#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  function countNum (l) {
    if (l === searchElement) {
      count += 1;
    }
  }
  list.forEach(countNum);
  return count;
};
