import heapq
# calculate heuristic value
def manhattan_dist(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)

#search algorithm
def a_star(row,col,starting_point,ending_point,maze_style):
    visited_node_track=[[False for _ in range(col)] for _ in range(row)]
    action=[(0,-1,"L"),(0,1,"R"),(-1,0,"U"),(1,0,"D")]
    PQ=[]
    actual_value_g=0
    heuristic_value_h=manhattan_dist(starting_point[0],starting_point[1],ending_point[0],ending_point[1])
    f=actual_value_g+heuristic_value_h
    heapq.heappush(PQ,(f,actual_value_g,starting_point[0],starting_point[1],''))

    while PQ:
        f,actual_value_g,x,y,path=heapq.heappop(PQ)
        if ending_point == (x,y):
            print(f"{actual_value_g}\n{path}")
            return
        if not(visited_node_track[x][y]):
            visited_node_track[x][y]=True
        else:
            continue

        for dx,dy,action_move in action:
            newX,newY=x+dx,y+dy
            if 0<=newX<row and 0<=newY<col:
                if maze_style[newX][newY]=="0" and not visited_node_track[newX][newY]:
                    new_actual_value_g=actual_value_g+1
                    new_heuristic_value_h=manhattan_dist(newX,newY,ending_point[0],ending_point[1])
                    newF=new_actual_value_g+new_heuristic_value_h
                    heapq.heappush(PQ,(newF,new_actual_value_g,newX,newY,path+action_move))
    print(-1)

        

    
# input function
def input_functions():
    row,column=input().split()
    row_number,column_number=int(row),int(column)
    x0,y0=input().split()
    starting_point=tuple((int(x0),int(y0)))
    x2,y2=input().split()
    ending_point=tuple((int(x2),int(y2)))
    maze_style=[list(input().strip()) for _ in range(row_number)]

    a_star(row_number,column_number,starting_point,ending_point,maze_style)

input_functions()



