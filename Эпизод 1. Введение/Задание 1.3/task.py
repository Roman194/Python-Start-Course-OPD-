# Пример 1
def task_1(n):
    # TODO
    x=1
    res=0
    while(x<11):
        res+=1/x
        x+=1
    return res


# Пример 2
def task_2(x, n):
    # TODO
    z=1
    res=0
    while z<=17:
        res+=x/z
        z+=2
    return res


# Пример 3
def task_3(n):
    # TODO
    i=1
    res=1
    while(i<=n):
        res*=i
        i+=1
    return res


# Пример 4
def task_4(x, n):
    # TODO
    x=1
    y=1
    for i in range(2,n+1):
        x*=(y+i)/i
    return x


# Пример 5
def task_5(x, n):
    # TODO
    x=0
    y=1
    for i in range(1,n+1):
        x+=(y*i)/(i*2)
    return x


# Пример 6
def task_6(n):
    # TODO
    res=1
    i=2
    while i<=20:
        res*=i
        i+=2
    return res
