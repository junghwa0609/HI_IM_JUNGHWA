#(1,1) (1,2) (1,3)
#(2,1) 
#            (3,3)

N=int(input())
plan = list(input().split())

a=0

first=[1,1]
L = first[1] -1
R = first[1] +1
U = first[0] -1
D = first[0] +1

for i in range(N):
    num =plan.count(plan[i])
    first = num*plan[i]
    if (first[1] or first[0]) >= N : (first[1] or first[0])==N
    elif (first[1] or first[0]) <=1 : (first[1] or first[0]) ==1
    
print(first)

#구현 실패