/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */

var numMatchingSubseq = function (S, words) {
  let map = new Map();
  for (let s of S) {
    map.set(s, []);
  }
  for (let w of words) {
    if (map.has(w[0])) map.get(w[0]).push({ word: w, idx: 0 });
  }
  let count = 0;
  for (let s of S) {
    let words = map.get(s);
    let len = words.length;
    for (let i = 0; i < len; i++) {
      let w = words.shift();
      if (w.idx === w.word.length - 1) {
        count++;
      } else {
        w.idx++;
        if (map.has(w.word[w.idx])) map.get(w.word[w.idx]).push(w);
      }
    }
  }
  return count;
};

const s = "abcde",
  words = ["a", "bb", "acd", "ace"];
console.log(numMatchingSubseq(s, words));
