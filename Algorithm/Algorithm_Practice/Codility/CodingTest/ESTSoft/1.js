function solution(A){
    let Counter = {};
    for(let i =0 ; i < A.length ; i++){
        if(Counter[A[i]] === undefined){
            Counter[A[i]] = 0;
        }
        Counter[A[i]] +=1;
    }
    
    let Max = 0;
    let keys = Object.keys(Counter);
    keys.forEach((key)=>{
        if(key == Counter[key]){
            Max= Math.max(Max,key);
        }
    })
    return Max;
}
A = [3,8,2,3,3,2];
B = [7,1,2,8,2];
C = [3,1,4,1,5];
D = [5,5,5,5,5];
console.log(solution(B));