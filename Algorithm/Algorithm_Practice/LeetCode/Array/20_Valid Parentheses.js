// 20. Valid Parentheses
var isValid = function (s) {
  const stack = [];
  const mapping = {
    ")": "(",
    "}": "{",
    "]": "[",
  };
  if (s.length === 1 || s.length === 0) return false;
  for (let char of s) {
    if (!mapping.hasOwnProperty(char)) stack.push(char);
    else {
      const lastChar = stack[stack.length - 1];
      if (mapping[char] === lastChar && stack.length > 0) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  if (stack.length > 0) return false;
  else return true;
};
const s = "((";

console.log(isValid(s));
