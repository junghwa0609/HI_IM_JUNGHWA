#큐는 먼저들어온게 먼저 나간다.
#스택은 나중에 들어온게 먼저 나간다.


from collections import deque #큐 구현을 위해 deque라이브러리를 사용해야한다
#리스트를 사용해도 되지만 시간복잡도가 높아지므로 꼭 덱 라이브러리를 사용하도록!
queue = deque()
#삽입은 어팬드, 삭제는 팝레프트(먼저 들어온게 왼쪽 나중에 들어온게 오른쪽이니까 왼쪽부터 삭제!)

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()#역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력된다.