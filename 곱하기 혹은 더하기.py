#각 자리가 한자리 숫자로 이루어진 문자열 S가 주어졌을떄
#왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인해서
#숫자 사이에 x혹은 +연산자를 넣어서
#결과적으로 만들어질 수 있는 가징 큰 수를 구하는 프로그램
#+든, x든 왼쪽에서부터 순서대로 이루어진다.
#다시! 0과 1을 만나면 더하기!
#나머지 수를 만나면 곱하기!

S = list(map(int,input()))
result = 0

for i in range(len(S)):
    if S[i] == 0 or S[i]==1 or result==0 :
        result += S[i]
    else :
        result *= S[i]

print(result)