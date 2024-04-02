input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0])) - int(ord('a'))+1 #ord는 해당하는 문자를 해당하는 숫자로 바꿔서 출력함
#나이트가 이동할 수 있는 8가지 방향 정의 (dx,dy정하는거 말고도 다른 방법을 써봄)
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] #01이렇게 쓰면 오류난다

#8가지 방향에 대해 각 위치로 이동이 가능한지 확인!
result = 0
for step in steps:
    #이동하고자 하는 위치를 확인해준다.
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <=8 and 1<=next_column<=8:
        result +=1

print(result)