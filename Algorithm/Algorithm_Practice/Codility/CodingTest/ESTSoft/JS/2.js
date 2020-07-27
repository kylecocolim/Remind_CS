function solution(A){
    if(A.length <= 1){
        return -1
    }
    else{
        let C = {};
        for(let i = 0 ; i<A.length ; i++){
            let B = A[i].toString();
            
            let tmpSum = 0; 
            for(let j =0 ; j<B.length;j++){
                tmpSum += Number(B[j]);
            }
            let tmpArray = [tmpSum];
            if(C[tmpSum] === undefined){
                C[tmpSum] = [];
            }
            C[tmpSum].push(A[i]);
        }
        let keys = Object.keys(C);
        let MaxNum = 0;
        keys.forEach((key)=>{
            if(C[key].length >= 2){
                let sortedArr = C[key].sort().reverse()
                MaxNum = Math.max(MaxNum,sortedArr[0]+sortedArr[1]);
            }
        })
        if(MaxNum > 0){
            return MaxNum;
        }
        else{
            return -1;
        }
    }
}

A = [51,71,17,42];
B = [42,33,60];
C = [51,32,43];
console.log(solution(B));