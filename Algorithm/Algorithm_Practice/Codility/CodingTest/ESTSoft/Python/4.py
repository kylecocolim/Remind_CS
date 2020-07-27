
def solution(S,C):
    if len(S) > 0:
        peoples = S.split(';')
        emails = []
        emailsDict = dict()
        result = ''
        for name in peoples:
            nameSplit = name.split(' ')
            firstName = nameSplit[0]
            if firstName == '':
                firstName= nameSplit[1]
            firstName = firstName.replace('-','').lower()
            lastName= nameSplit[-1].replace('-','').lower()
            email = lastName+'_' + firstName + '@' + C.lower() + '.com'
            if email not in emailsDict.keys():
                result += name + ' <'+email +'>;'
                emailsDict[email] =1
            else: 
                emailsDict[email] += 1
                email = lastName+'_' + firstName + str(emailsDict[email]) + '@' + C.lower() + '.com'
                result += name + ' <'+email +'>;'

        return result[:-1]
    else:
        return ''
S = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brain Parker"
C = 'example'
print(solution(S,C))