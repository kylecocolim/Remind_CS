# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    incompletion = ""
    player = dict()

    for name in participant:
        try:
            player[name] +=1 
        except:
            player[name] = 1
    
    for complete_name in completion:
        if complete_name in player.keys():
            player[complete_name] -=1

    for name, count in player.items():
        if count > 0:
            incompletion = name

    return incompletion        
        
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

participant2 = ["mislav", "stanko", "mislav", "ana"]
completion2 = ["stanko", "ana", "mislav"]

print(solution(participant2,completion2))
