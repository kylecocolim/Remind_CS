function solution(A){
    function isZigZag(treeSkyline){
        let direction = '';
        for(let i= 0 ; i< treeSkyline.length - 1 ; i++){
            if(treeSkyline[i] < treeSkyline[i+1]){
                if(direction != ''){
                    if(direction === 'UP'){
                        return false;
                    }
                    else{
                        direction = 'UP';
                    }
                }
                else{
                    direction = 'UP'
                }
            }
            else if(treeSkyline[i] > treeSkyline[i+1]){
                if(direction != ''){
                    if(direction === 'Down'){
                        return false;
                    }
                    else{
                        direction = 'Down';
                    }
                }
                else{
                    direction = 'Down'
                }
            }
            else{
                // Same Height 
                return false;
            }
        }
        return true;
    }

    if(isZigZag(A) == true){
        return 0;
    }
    let cnt = 0;
    for(let i = 0 ; i < A.length ; i++){
        let tmpTreeline = A.slice();
        tmpTreeline.splice(i,1);
        if(isZigZag(tmpTreeline)===true){
            cnt+=1;
        }   
    }
    if (cnt === 0){
        return -1;
    }
    else{
        return cnt;
    }
}

A = [3,4,5,3,7];
B = [1,2,3,4];
C = [1,3,1,2];
console.log(solution(C));