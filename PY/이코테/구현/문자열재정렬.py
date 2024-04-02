S= str(input())
S = sorted(S)
result = []
sum = 0
for i in range(len(S)):
    if S[i].isalpha() == True:
        result.append(S[i])
    else :
       sum += int(S[i]) 

if sum != 0 : result.append(str(sum))

print(''.join(result)) #join을 몰랐음 !! 리스트를 문자열로 출력할땐 조인을 쓸 것!K1KA5CB7