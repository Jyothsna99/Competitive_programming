'''The maze looks like this:
    **********Refer EPAM_Shinchan.png**********

In the maze, you start at the top left 1,1, and make your way down to n,n. At each step, you are only allowed 3 moves:

You can move to the right (east)
You can move down (south)
If you are on the left diagonal (row number and column number are same), then you can move down and right (south-east) in one move
However, you cannot move to the block if it is an obstacle. You can only move if there is a path. 1 denotes an obstacle and 0 the path.

You have to print the minimum number of steps to reach the destination (bottom-right) from the starting position (top-left).

In the above diagram, the minimum number of steps required is 3 steps:

Step 1: (1,1) -> (2,2)
Step 2: (2,2) -> (3,3)
Step 3: (3,3) -> (4,4)
Input format
The first line contains T the number of test cases
Each test case contains n and n, the number of rows and columns (it is always a square maze)
This is followed by n space separated numbers in n lines
Output format
For each test case, print the minimum number of steps required to reach the destination
Note: the start and destination will always be marked as 0 in the map

Example Input

2
3 3
0 1 1
1 0 1
0 0 0
4 4
0 0 0 1
0 0 1 0
0 0 1 0
1 0 0 0
Example Output

2
5
Explanation

In first case, move along the diagonal and you will reach the destination in 2 steps
The steps are: (1,1) -> (2,2); (2,2) -> (3,2); (3,2) -> (4,2); (4,2) -> (4,3); (4,3) -> (4,4)
'''
t=int(input())
for i in range(t):
    n=5
    maze=[[0, 1, 1, 1,1], [1, 0, 0, 0,1], [0, 0, 1, 0,0], [0,0, 0, 1, 0],[0,0,0,1,0]]
    '''for i in range(n):
        maze.append(list(map(int,input().split())))'''
    i=0
    j=0
    count=0
    while(i<n-1 and j<n-1):
        if i==j and maze[i+1][j+1]==0:
            i=i+1
            j=j+1
            count+=1
        elif maze[i+1][j]==0:
            maze[i+1][j]=2
            i=i+1
            count+=1
        elif maze[i][j+1]==0:
            maze[i][j+1]=2
            j=j+1
            count+=1
        else:
            if maze[i][j-1]==2:
                count-=1
                j=j-1
            elif maze[i-1][j]==2:
                count-=1
                i=i-1
            elif maze[i+1][j]==2 and maze[i][j+1]==2 and maze[i][j-1]==0:
                count-=1
                i=i-1
            else:
                count-=1
                j=j-1
            
        if i==n-1 and j<n-1:
            while(j<n-1):
                if maze[i][j+1]==0:
                    maze[i][j+1]=2
                    j=j+1
                    count+=1
                else:
                    while(maze[i][j-1]==2):
                        count-=1
                        j=j-1
                    count-=1
                    i=i-1
                    break
                print(i,j)
        elif i<n-1 and j==n-1:
            while(i<n-1):
                if maze[i+1][j]==0:
                    maze[i+1][j]=2
                    i=i+1
                    count+=1
                else:
                    while(maze[i-1][j]!=2):
                        count-=1
                        i=i-1
                    count-=1
                    j=j-1
                    break
        print(i,j)
    print(count)
        




