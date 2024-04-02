def solution(number,k):
    collected = []
    for i , num in enumerate(number): # enumerate는 인덱스와 원소로 이루어진 튜플을 만들어 준다. number안의 숫자와 인덱스가 나온다(숫자는 문자열로 안되고 숫자 그대로 나오나봄..)
        while len(collected) >0 and collected[-1] <num and k>0 : #2. 첫번째숫자가 담겨있고, 첫번째 수가 두번째 수보다 작으며 k가 0보다 클 때
            collected.pop() #3. 첫번째 숫자를 다시 빼내고
            k -= 1 #4. 숫자 한개 뺐으니까 뺄 수 하나 줄어듬
        if k == 0 : #만약에 모두 다 뺐다면
            collected += list(number[i:]) #현재 숫자부터는 다 들어가야함
            break #그리고 끝내자
        collected.append(num) #1. 첫번째 숫자를 담는다. 5. 두번째 숫자가 담긴다.

    collected = collected[:-k] if k>0 else collected #number을 끝까지 돌았는데, k가 남아있을땐, 맨 뒤에서부터 k개 빼준다. 그게 아니라면 collected = collected
    answer = ''.join(collected)
    return answer
print ( solution("4177252841",4))