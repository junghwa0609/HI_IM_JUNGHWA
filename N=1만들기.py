N=25
K=3
count =0


for i in range(N):
    if N%K == 0:
        count += 1
        N /= K
        if N==1:break
    else :
        count +=1
        N -= 1
        if N==1:break
    
print(count)