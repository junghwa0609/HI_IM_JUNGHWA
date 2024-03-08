#(1,1) (1,2) (1,3)
#(2,1) 
#            (3,3)
'''
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
'''

#3월 5일에
#구현 성공!!
#시작좌표는 항상 1,1
#계획서에는  LRUD 중 하나의 문자가 반복적으로 적혀있따
#계획서를 보고 최종 여행가가 도착할 위치를 출력하는 프로그램 작성

A = int(input())
B = list(input().split())

where = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
start_where = [1,1]
for alpha in B :
  if alpha in where :
    start_where[0]+= where[alpha][0]
    start_where[1]+= where[alpha][1]

    if (start_where[0] and start_where[1]) > A or (start_where[0] and start_where[1])<1 :
      start_where[0]-= where[alpha][0]
      start_where[1]-= where[alpha][1]


print(start_where)
