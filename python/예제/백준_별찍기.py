def draw_stars(n):
    if n==1:
        return ['*']

    Stars=draw_stars(n//3)
    L=[]

    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        L.append(star*3)

    return L

N=int(input())
print('\n'.join(draw_stars(N)))

#거의 다 도달했는데 못풀었다.. 다음부턴 이 패턴을 더 잘 익혀야 겠다.