// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
// Problem Number : 1351
var countNegatives = function(grid) {
    const row = grid.length;
    let negativeResults = 0;
    for(let i= 0; i < row ; i++){
        grid[i].forEach((key)=>{
            if(key<0){
                negativeResults +=1;
            }
        })
    }
    return negativeResults
};