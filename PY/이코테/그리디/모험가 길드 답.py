n=int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 #총 그룹 수 
count = 0 #현재 그룹에 포함된 모험가의 수 - 나는 이거 안설정했는데..

for i in data:
    count +=1
    if count >= i : #현재 그룹에 포함된 모험가의 수가 i 이상이면, 그룹을 만들어준다
        result +=1
        count=0 #그리고 그룹은 초기화된다.

print(result)
