# 1. 재귀함수를 쓰지않고 만들기


def jg():
    print(" 몇 팩토리얼을 구할까요? ",end=" : ")
    A = input()
    a = ''.join(char for char in A if char.isdigit()) #isdigit은 숫자면 트루를, 아니면 false를 반환한다
    answer = 1

    if int(a) == 0 or int(a) == 1 : return print(a)
    
    for i in range(1,int(a)+1):
        answer *= i
    
    return print(answer)
'''
jg()'''

# 2. 재귀함수를 써서 만들기

print(" 몇 팩토리얼을 구할까요? ",end=" : ")
A = input()
a = ''.join(char for char in A if char.isdigit()) #isdigit은 숫자면 트루를, 아니면 false를 반환한다
answer = 1

def jgg(k):
    i= int(k)
    if int(i) == 0 or int(i) == 1 : return print(i)

    return i*jgg(i-1)

jgg(a)