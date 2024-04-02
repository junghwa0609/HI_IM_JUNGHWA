n=int(input())
x,y = 1,1
plans= input().split()

dx=[0,0,-1,1] #x축을 통해 이동하는 방법은 왼쪽, 오른쪽! [위, 아래, 왼, 오]
dy=[-1,1,0,0]
move_types = ['L','R','U','D']

#받은 이동계획을 하나씩 확인하기
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i] #이러면 같은 숫자라고 해도 x값만 증감하거나 y값만 움직임
            ny = y + dy[i] 
    if nx<1 or ny<1 or nx>n or ny>n:
        continue #x,y값에 nx,ny안넣고 다시 첫번째 for문으로 돌아간다.
    x,y=nx,ny #두번째 if문에 안걸린 애들만 x,y에 저장된다.

print(x,y)
# 따라치는것도 제대로 못함.. 너무 오래 화면을 쳐다봐서 그런거니?
