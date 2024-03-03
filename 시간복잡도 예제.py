import random
findNumber = random.randrange(1,101) #1~100 사이 랜던값 생성

for i in range(1,101):
    if i== findNumber:
        print(i)
        break