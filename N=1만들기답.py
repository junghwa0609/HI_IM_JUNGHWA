n,k=map(int,input().split()) # 나는 인풋을 받는게 아니고 내가 직접 입력했다. 인풋 연습
result=0 #내꺼 count랑 똑같은 역할

while True:
    target = (n//k)*k #n에서 1을 몇번 빼면 k로 나누어떨어지는지 가장 큰 수 구하는 식
    result += (n-target) #그 수를 n에서 빼면 1을 몇번 뺐는지 알 수 있다. 그만큼 1빼기를 진행했다는것
    n=target #1을 다 빼고나서 k로 나누어떨어지는 n을 이제 n으로 넣어주고 
    result +=1 # 나누기 할거니까 한번 더해주고
    n//=k #n은 이제 k로 나누어서 그 숫자로 넣어준다. 그리고 윗 단계들 반복
    if n<k:
        break #n을 더이상 k로 나눌 수 없을 때, 반복문을 탈출한 뒤 1이 될때까지 빼준다.

result += (n-1) #1될때까지 1씩 빼주는 횟수를 더해주고
print(result) #결과 값 출력