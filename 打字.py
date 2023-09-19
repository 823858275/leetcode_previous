# def numPair(n,nums):
#     for i in range(n):
#         res=nums[i]
#         for j in range(n):
#             if (res[0]==nums[j][0] or res[1]==nums[j][1]) and (j!=n-1):
#                 continue
#             elif (j==n-1) and (res[0]==nums[j][0] or res[1]==nums[j][1]):
#                 return res
#             else:
#                 break
#     return "No"
def numPair(n,nums):
    for i in range(1,10**9+1):
        for j in range(1,10**9+1):
            for k in range(n):
                if (nums[k][0]==i or nums[k][1]==j) and k==n-1:
                    return (i,j)
                elif (nums[k][0]==i or nums[k][1]==j) and k!=n-1:
                    continue
                else:
                    break
    return "No"
print(numPair(4,[(1,5),(3,5),(1,3),(5,5)]))
# import sys
# line = sys.stdin.readline().strip()
# n=int(line)
# nums=[]
# for i in range(n):
#     line=sys.stdin.readline().strip()
#     values = tuple(map(int, line.split(" ")))
#     nums.append(values)
# print(numPair(n,nums))