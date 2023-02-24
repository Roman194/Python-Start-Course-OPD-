def task_1(N):
    # TODO
    res=1
    for i in range(2,N+1):
        res*=i
    return res


def task_2(N):
    # TODO
    res=0
    last_el=1
    prelast_el=0
    for i in range(2,N):
        res=last_el+prelast_el
        prelast_el=last_el
        last_el=res
    return res


def task_3(N):
    # TODO
    res=[]
    if N>0:
        for i in range(1,N+1):
            if N%i == 0:
                res.append(i)
    return res
