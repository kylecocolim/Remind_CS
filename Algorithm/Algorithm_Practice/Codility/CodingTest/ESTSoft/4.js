function solution(S,C){
    if(S.length >= 1){ 
        let emailDict = {};
        let peoples = S.split(';');
        let result = '';
        for(let i = 0 ; i<peoples.length ; i++){
            let emails = Object.keys(emailDict);
            let name = peoples[i].split(' ');
            let lastName = name[0].toLowerCase();
            if(name[0] === ''){
                lastName= name[1].toLowerCase();
            }
            let firstName = name[name.length-1].replace('-','').toLowerCase();
            email = lastName + '_' + firstName + '@' + C.toLowerCase() + '.com';
            if(emails.indexOf(email) === -1){
                emailDict[email] = 2;
                result += `${peoples[i]} <${email}>;`
            }
            else{
                let cnt = emailDict[email];
                emailDict[email] +=1;
                email = lastName + '_' + firstName + cnt + '@' + C.toLowerCase() + '.com';
                emailDict[email] +=1;
                result += `${peoples[i]} <${email}>;`
            }
        }
        return (result.slice(0,result.length-1));
    }
    else{
        return '';
    }
}
S = "John Doe; Peter Benjamin Parker; John Elvis Doe; Mary Jane Watson-Parker; John Evan Doe; Jane Doe; Peter Brain Parker";
C = 'Example';
console.log(solution(S,C));