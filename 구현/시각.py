#정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각중
#3이 하나라도 포함되는 모든 경우의 수 구하는 프로그램 작성
#문자열을 각각 or로 처리할 게 아니고 다 합쳐서 그중에 3이 있나 확인 -> +를 사용해서 문자열을 잇는다
N = int(input())

timeh = range(N+1)
timem = range(60)
times = range(60)
result=0
for h in timeh:
    for m in timem: 
        for s in times:
            if '3' in str(h) + str(m) + str(s):
                result +=1

print(result)

#정답과 같아서 따로 정답을 쓰진 않겠다.