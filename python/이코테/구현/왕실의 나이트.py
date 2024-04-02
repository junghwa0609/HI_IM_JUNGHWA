#나이트의 이동방향 정해주기
#나이트가 이동 할 수 있는 경우의 수 정해주기(총 8가지 방향 가능)

A = list(input()) #시작위치
A[1] = ord(A[0])-ord('a')+1
A[0] = int(A[0])
'''
U:(-2,-1)
L:(-2,-1)
R:(2,1)
D:(2,1)
'''
LRUD = {(-2,-1),(2,1)}
where = []

for i in range(2) :
  where+ list(LRUD[i][0], LRUD[i+1][1]) + list(LRUD)
  LRUD[i] LRUD[i]

for i in range(2):
  if LRUD[]