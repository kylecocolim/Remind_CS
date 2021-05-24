/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var isSubsequence = function (s, t) {
  if (s.length > t.length) return false;
  s = s.split("");
  for (let char of t) {
    if (s[0] === char) {
      s.shift();
    }
  }
  return s.length === 0 ? true : false;
};

const s = "",
  t = "";
console.log(isSubsequence(s, t));
