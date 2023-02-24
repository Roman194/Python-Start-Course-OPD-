def task_1(str):
    # TODO
    slovar={}
    for sym in str:
        if sym!=' ' and sym!='1':
            if sym in slovar:
                slovar[sym]+=1
            else:
                slovar[sym]=1

    return slovar


def task_2(list):
    # TODO
    summ=0
    list=set(list)
    summ=sum(list)
    return summ


def task_3(cities):
    # TODO
    str=", ".join(cities)
    str+="."
    return str


def task_4(a, b):
    # TODO
    c=[]
    for sym in a:
        for o_sym in b:
            if sym==o_sym:
                c.append(sym)

    c=set(c)
    c=list(c)

    return c
