
def solution(jobs):
    time = 0
    queue = []  
    process = []
    isRunning = False
    timer = 0
    idx = 0

    if len(jobs) > 0:
        while True:
            if timer == 0 and isRunning == True and len(jobs) > idx:
                process.append([jobs[idx][1],time])
            # Queue
            if timer == 0 and len(queue) == 0:
                isRunning = False
            # Job이 끝남 , Queue 없음 , 현재 돌아가는 프로세스 없음 
            if len(jobs) == idx and len(queue) == 0 and isRunning == False:
                #return time 
                break

            # Job이 있으면 time == 인 Queue에 Job넣기    
            if len(jobs) > idx:
                if jobs[idx][0] == time:
                    queue.append(jobs[idx])
                    if len(queue) >= 2:
                        queue = sorted(queue, key= lambda x:x[1])
                    # Job Index
                    idx +=1

            # Timer에 Queue 넣기
            if timer == 0 and len(queue) > 0:
                isRunning=False
                timer = queue.pop(0)[1]
            
        
            if timer != 0:
                isRunning=True
                timer -=1

            # Terminate
            time +=1
        print(process)
        print(sum(process)/len(jobs))
jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)