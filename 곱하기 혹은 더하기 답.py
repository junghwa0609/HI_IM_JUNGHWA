data = input()

#첫 번째 문자를 숫자로 변경하여 대입

result = int(data[0])
for i in range(1,len(data)):
    num = int(data[i])
    if num <=1 or result <=1: # 부등호를 사용했어도 좋았을 것 같다. 그리고 result가 1일 경우도 생각 못했다
        result += num
    else:
        result *= num
print(result)

#이번문제는 부등호 빼고 거의 똑같았다!
