var containsDuplicate = function(nums) {
    let table = new Map();
    for(let num of nums){
        if(table.has(num) !== false) return true;
        else{
            table.set(num,1);
        }
    }
    return false;
};

const nums = [1,2,3,1];
const nums2 = [1,1,1,3,3,4,3,2,4,2]
const nums3 = [1,2,3,4]
console.log(containsDuplicate(nums3));