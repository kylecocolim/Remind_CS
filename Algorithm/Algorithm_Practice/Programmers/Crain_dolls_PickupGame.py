# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
# Failed and Suceess 2 TestCases
def solution(board,moves):
    def SearchingTops(board,tops):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != 0 and tops[col] == 0:
                    tops[col] = row 
    
    def bucketupdate(board,col_tops,move):
        row = col_tops[move-1]
        col = move-1
        col_tops[move-1] += 1
        return board[row][col]
    
    def isgetScore(score,bucket):
        while True:
            if len(bucket) >=2:
                if bucket[-2] == bucket[-1]:
                    bucket.pop(len(bucket)-1)
                    bucket.pop(len(bucket)-1)
                    score+=2
                else:
                    return score
            else:
                return score
    col_tops = [0 for i in range(len(board))]
    SearchingTops(board,col_tops)    
    bucket = []
    score = 0
    for move in moves:
        if col_tops[move-1] < len(board):
            bucket.append(bucketupdate(board,col_tops,move))
            if len(bucket) >=2:
                score = isgetScore(score,bucket)
    return score

board =[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4] 
solution(board,moves)
