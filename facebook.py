'''In Pikachu's map, the time taken between any island i and j is the absolute difference between i and j. So if there are are 5 islands, the walking time between them is:

From 1 to 2, time is 1 mins, to 3 the time is 2 mins and so on...
Similarly, the distance between 3 and 5 is 2 mins and so on...
Additionally, below is Oggy's map (via ships). It contains the time by ship between any 2  i and j

1 2 10
1 5 1
That is, there are 2 ships available. The ship between 1 and 2 takes 10 mins. But between 1 and 5 the time is 1 mins.

Thus, to reach 6, the best thing to do is to take a ship to 5 and then walk to 6

Taking your start point as 1 and end point as D, and given the schedule of N ships, you need to find the minimum time taken to reach home.

Note: You can only go forward, not backward.

Input format
The first line of input contains T, the number of test cases
The first line of each test case is D -  the destination
This is followed by N - the number of ship routes
After that, N lines of 3 numbers which signify start position, end position and time taken between the positions
Output format

For each test case, print the minimum time taken to reach the destination
Example Input
2
6
3
2 6 3
1 4 2
2 5 1
10
5
3 7 10
3 5 2
6 10 1
5 7 3
2 4 2
Example Output
3
6
Explanation
In the first case, the shortest path is to:
walk from 1 to 2: 1 minutes
ship from 2 to 5: 1 minutes
walk from 5 to 6: 1 minutes
Total: 3 minutes
In the second case, the best path is to:
walk from 1 to 3: 2 minutes
ship from 3 to 5: 2 minutes
walk from 5 to 6: 1 minutes
ship from 6 to 10: 1 minutes
Total: 6 minutes'''
t=int(input())
for i in range(t):
    d=int(input())
    n=int(input())
    m=[]
    for i in range(n):
        m.append(list(map(int,input().split())))
    s={}
    for i in range(len(m)):
        if m[i][1]-m[i][0]>m[i][2]:
            s[(m[i][0]-1,m[i][1]-1)]=m[i][2]
    V = d
    graph=[[0 for column in range(V)]  
                    for row in range(V)] 
    for i in range(V):
        for j in range(V):
            if (i,j) in s:
                graph[i][j]=s[(i,j)]
            elif j>i:
                graph[i][j]=j-i
    
    def minDistance(dist, sptSet): 
        min = d+1
        for v in range(V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index 
  
    def dijkstra(src): 
        dist = [d+1] *V 
        dist[src] = 0
        sptSet = [False] *V 
  
        for cout in range(V): 
            u = minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(V): 
                if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] +graph[u][v]: 
                    dist[v] = dist[u] + graph[u][v]
        print(dist)
    dijkstra(0)