'''Nobita has a specific medicine to solve this problem. He tried to say the name of the medicine, but his sentences are jumbled beyond imagination.

Here is how you can help him:

His sentence is in the form of a very long word. mymedicinesarerighthere
You need to break this word down in the following way: m, ym ,edi ,cine ,sarer ,ighthe, re
Then take the first and last characters of the sub-words as long as the sub-word is longer than the previous sub-word: m, ym, ei, ce, sr, ie. Notice we don't touch re because it is shorter than the previous sub-word
The words on joining gives the name of Nobita's medicines: mymeicesrie
Input Format
The first line contains T, the number of test cases
This is followed by T strings (with length >=1)

Output format:

Print the name of Nobita's medicines

Example Input:

3
mymedicinesarerighthere
isnobitaalive
testcasesoftenmakemuchmoresensethanthisone

Example Output:

mymeicesrie
isnoitl
testasofmachent'''

t=int(input())
for i in range(t):
    s=input()
    ans=[]
    o=""
    ans.append(s[0])
    o+=ans[0]
    k=1
    l=1
    while(k<len(s)):
        ans.append(s[k:k+l+1])
        k=k+l+1
        l+=1
    for i in range(1,len(ans)-1):
        o+=(ans[i][0]+ans[i][-1])
    if len(ans)>1 and len(ans[-1])>len(ans[-2]):
        o+=(ans[-1][0]+ans[-1][-1])
    print(o)
        
        
        
        
        
        
