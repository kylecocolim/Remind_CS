// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Tag : String , SubString , Sliding Window 

var lengthOfLongestSubstring = function(s){
    function isRepeating(subString){
        let charArr = [];
        for(let i = 0 ; i< subString.length ; i++){
            if(charArr.indexOf(subString[i]) === -1){
                charArr.push(subString[i]);
            }else{
                return false;
            }
        }
        return true;
    }

    /*
    Time Exceed !
    for(let windowSize = 1 ; windowSize < s.length + 1; windowSize ++){
        for(let ptr = 0 ;  ptr < s.length - windowSize +1 ; ptr ++){
            if(isRepeating(s.slice(ptr,ptr+windowSize)) === true){
                result = windowSize;
            }
        }
    }
    */

    const seen = new Map();
    let start = 0;
    let maxLen = 0;
    
    for(let i = 0; i < s.length; i++) {
        if(seen.has(s[i])) start = Math.max(seen.get(s[i]) + 1, start)
        seen.set(s[i], i);
        maxLen = Math.max(i - start + 1, maxLen);
        console.log(start, maxLen);

    } 
    console.log(seen);
    return maxLen;  
}

const s = 'pwwkew';
result = lengthOfLongestSubstring(s);
console.log(result);