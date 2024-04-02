# 가치 V만큼 즐길 수 있음. K>=W*N 즐길 수 있는 최댁값 = V*N

#몇종류N인지 최대무게K
#    W     V
#1. 6키로, 13가치
#2. 4키로, 8 가치
#여러줄을 입력받는 법!import sys / sys.stdin.readline
'''
import sys
N, K = map(int, sys.stdin.readline().split())
list_ho = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Value = []
for i in range(N-1):
    for j in range(i+1,N):
        if (a[i][0]+a[j][0]) <= K :
            Value.append(a[i][1]+a[j][1])
print(max(Value))'''

#냅색 알고리즘 : 한 도둑이 훔치는 배낭에 담ㅁ을 수 있는 문제의 최댓값이 정해져 있음.
#일정 가치와 무게가 있는 짐을을 배낭에 넣을 때, 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾자!
#이번 문제는 담을 수 있는 물건이 나누어질 수 없는 경우이다.
#X축에는 1~K까지 무게, y축은 물건N개의 개수만큼 배열을 만들어준다.
#행을 차례로 돌면서 현재 돌고있는 무게보다 지금 물건이 작으면 