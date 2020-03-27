# https://www.acmicpc.net/problem/13460
# tag : DFS 

def Solution(arr,n,m):
    def dfs(maps,red_start,blue_start):
        def Direction(visited):
            p_row = int(visited[-2] / n )
            p_col = visited[-2] %m 
            c_row = int(visited[-1] /n )
            c_col = visited[-1] %m 
            row_calc = p_row - c_row 
            col_calc = p_col - c_col 
            if row_calc == 1:
                return 'U'
            if row_calc == -1:
                return 'D'
            if col_calc == 1:
                return 'R'
            if col_calc == -1:
                return 'L'

        count = 1
        red_stack = list() 
        red_stack.append(red_start)
        red_visited = list()
        red_PastDirection = str()

        blue_stack = list() 
        blue_stack.append(blue_start)
        blue_visited = list()
        blue_PastDirection = str()
        while red_stack or blue_stack:
            if len(red_stack) > 0:
                red_node = red_stack.pop()
            if len(blue_stack) > 0:
                blue_node = blue_stack.pop()
            if maps[blue_node] == 'O':
                return -1
            if maps[red_node] == 'O':
                if count > 10:
                    return -1
                else:
                    return count
            

            # Red_Bullet
            if (maps[red_node] == '.' or maps[red_node]=='R') and red_node not in red_visited:
                row = int(red_node/n)
                col = red_node%m
                red_visited.append(red_node)
                if len(red_visited) == 2:
                    red_PastDirection =Direction(red_visited)
                if len(red_visited) >=3:
                    CurrentDirection = Direction(red_visited)
                    if red_PastDirection != CurrentDirection:
                        count +=1 
                    red_PastDirection = CurrentDirection                      
                if row < (n -1) :
                    red_stack.append(m*(row+1)+col)
                #Move Up
                if row > 0:
                    red_stack.append(m*(row-1)+col)
                #Move Right
                if col < (m-1):
                    red_stack.append(row*(m)+col+1)
                #Move Left
                if col > 0:
                    red_stack.append(row*m+col-1)

            ### Blue Bullet
            if (maps[blue_node] == '.' or maps[blue_node]=='B') and blue_node not in blue_visited:
                row = int(blue_node/n)
                col = blue_node%m
                blue_visited.append(blue_node)
                if len(blue_visited) == 2:
                    blue_PastDirection =Direction(blue_visited)
                if len(blue_visited) >=3:
                    CurrentDirection = Direction(blue_visited)
                    if blue_PastDirection != CurrentDirection:
                        count +=1 
                    blue_PastDirection = CurrentDirection                      
                if row < (n -1) :
                    blue_stack.append(m*(row+1)+col)
                #Move Up
                if row > 0:
                    blue_stack.append(m*(row-1)+col)
                #Move Right
                if col < (m-1):
                    blue_stack.append(row*(m)+col+1)
                #Move Left
                if col > 0:
                    blue_stack.append(row*m+col-1)    

    red_start = int()
    blue_start = int()

    for i in range(len(arr)):
        if arr[i] == 'R':
            red_start = i 
        if arr[i] == 'B':
            blue_start = i

    result = dfs(arr,red_start,blue_start)
    if result == None:
        return -1 
    else:
        return result

n = 7 
m = 7 
maps = "######..B##.#.##RO.######"
maps2 = "########..R#B##.######.....######.##O....########"
print(Solution(maps2,n,m))
