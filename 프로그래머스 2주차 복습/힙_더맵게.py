#try 1
'''
리스트 안의 숫자가 2개 이상 있는경우
정렬 후 [0],[1] pop
a=[0] +[1]*2
count+=1
a가 k보다 큰 경우 : 끝내기
a를 리스트 안에 넣고 리스트 다시 정렬
윗 단계들 반복

리스트 안의 숫자가 1개이고, 그 숫자가 k보다 크다면 return 0
아니라면 return -1
'''
def solution1(scoville, K):
    l = len(scoville)
    count = 0
    ho = [0]
    if l > 1 :
        while ho[0] < K :
            sorted(scoville)
            a = scoville.pop(0)
            b = scoville.pop(0) #여기서 pop 1을 하면 안된다. 이미 하나가 빠져나갔기 때문...
            c = a + b*2
            scoville.append(c)
            ho[0] = c
            count += 1
        return count
    elif l <= 1 and scoville[0] > K :
        return 0
    else :
        return -1 
    
'''결과
테스트는 통과했지만, 정확성테스트 9.5점.. 효율성0점. 뭐가 문제인지 강의를 들어보면서 찾아볼 것이다.
'''

#try 2 강의듣기
'''
새로 만든 음식의 자리를 찾을 땐, 이미 정렬되어있는 배열이므로 앞부터 맞는 자리를 찾아서 들어간다.
제일 작은 음식이 k보다 크면 된다. (나는 지금 만든 음식이 k보다 커야되는줄..)
최소, 최대 원소를 빠르게 꺼낼 수 있으면 좋겠는데!!!
힙(완전이진트리 - 앞서 배웠었다)
max heap 
min heap

Import heapq 
heapq.heapify(L) 리스트 L로부터 min heap 구성
m=heapq.heappop(L) min heap L에서 최소값 삭제(반환) (logn시간이 걸림)
heapq.heappush(L,x) min heap L에 원소 x 삽입 (logn시간이 걸림)
'''
import heapq
def solution2(scoville,K):
    heapq.heapify(scoville)
    answer = 0
    while True: #무한루프 형태로 만들기 1. 모든 음식의 스코빌지수가 K이상이 됐거나,2. 음식이 1개밖에 없을 때 K보다 작거나를 조건문에 쓰기보단 무한루프 break 하는게 더 편리
        min1 = heapq.heappop(scoville)
        if min1 >= K : #1. 모든 음식의 스코빌 지수 K이상
            break
        elif len(scoville) == 0: #2. 스코빌에 한개밖에 원소가 없었음 근데 K보다 작다
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2* min2
        heapq.heappush(scoville,new_scoville)
        answer += 1
    return answer

# 통과