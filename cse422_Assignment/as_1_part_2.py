import collections as c

def check_admissibility(node_number,edge_number,starting_node,goal_node,h,e):
    graph=c.defaultdict(list)
    for u,v in e:
        
        graph[v].append(u)
        graph[u].append(v)
    distance={dist:float('inf')for dist in range(1,node_number)}
    Q=c.deque([goal_node])
    distance[goal_node]=0
    while Q:
        current_node=Q.popleft()
        for child in graph[current_node]:
            if distance[child]==float('inf'):
                distance[child]=distance[current_node]+1
                Q.append(child)
    
    nodes_notadv=[]
    for n in range(1,node_number+1):
        if h[n]>distance[n]:
            nodes_notadv.append(n)
    if nodes_notadv:
        print(f"{0}\nHere nodes {', '.join(map(str,nodes_notadv))} are inadmissible.")
    else:
        print(1)
    

def input_function(h,e):
        node_number,edge_number=input().split()
        node,edge=int(node_number),int(edge_number)

        starting_node,goal_node=input().split()
        s_node,g_node=int(starting_node),int(goal_node)
        
        check_admissibility(node,edge,s_node,g_node,h,e)
    

# input 1
input_function({
                1: 3,
                2: 2,
                3: 1,
                4: 2,
                5: 1,
                6: 0
            },
         [
            (1, 2),
            (2, 3),
            (3, 6),
            (1, 4),
            (4, 5),
            (5, 6),
            (3, 5)
        ])

# input 2
input_function({
                1: 6,
                2: 4,
                3: 2,
                4: 5,
                5: 2,
                6: 0
            },
         [
            (1, 2),
            (2, 3),
            (3, 6),
            (1, 4),
            (4, 5),
            (5, 6),
            (3, 5)
        ])
