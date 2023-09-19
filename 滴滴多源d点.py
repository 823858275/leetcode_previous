def solution(n,sp,d,nums):
    if d==0:
        return 0
    if d>=n:
        return n
    tree=[]
    tree.append(1)
    child=1
    for i in range(n-1):
        parent=child
        child=nums.index(parent)+2
        tree.append(child)
    indexs=[]
    for s in sp:
        inx=tree.index(s)
        left=inx-d
        if left<=0:
            left=0
        right=inx+d
        if right>=len(tree)-1:
            right=len(tree)-1
        indexs.append([left,right])
    indexs.sort(key=lambda x:x[0])
    inter=indexs[0]
    for i in range(1,len(indexs)):
        if inter[1]<indexs[i][0]:
            return 0
        else:
            inter[0]=indexs[i][0]
    return inter[1]-inter[0]+1

import sys
line=sys.stdin.readline().strip()
n,m,d=list(map(int,line.split()))
line=sys.stdin.readline().strip()
sp=list(map(int,line.split()))
line=sys.stdin.readline().strip()
nums=list(map(int,line.split()))
print(solution(n,sp,d,nums))

