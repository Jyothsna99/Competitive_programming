'''Noddy's vehicle has 2 issues:

It needs exactly F amounts of fuel to fly this distance - not more and not less.
At a particular time, it cannot increase the fuel by more than K
There are N fuel stations on the way: each having A1 A2..... AN amount of fuel.

You have to tell us whether it is possible to fill the tank up to exactly F amounts.

Input Format
The first line contains T, the number of test cases. Each test case contains:
N, followed by N numbers denoting the amount of fuel at the ith station
F - the target fuel that you must reach
K - your limit for max fuel at one station
Output Format
Print Yes if you can fill with the given stations and capacities. Otherwise, print No

Sample Input
3
6 6 10 3 2 2 1
7
5
5 6 10 3 2 2
7
1
6 8 10 3 9 7 4 
2
10
Sample Output
Yes
No
No'''


t=int(input())
for i in range(t):
    n=list(map(int,input().split()))
    f=int(input())
    k=int(input())
    s=[]
    for i in range(1,len(n)):
        if n[i]<=k:
            s.append(n[i])
    c=len(s)
    subset=[[False for i in range(f+1)] for i in range(c+1)]
    for i in range(c+1):
        subset[i][0]=True
        for i in range(1,f+1):
            subset[0][i]=False
        for i in range(1,c+1):
            for j in range(1,f+1):
                if j<s[i-1]:
                    subset[i][j]=subset[i-1][j]
                if j>=s[i-1]:
                    subset[i][j]=(subset[i-1][j] or subset[i-1][j-s[i-1]])
    if subset[c][f]:
        print("Yes")
    else:
        print("No")
            
        




