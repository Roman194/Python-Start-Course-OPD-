import numpy as np

# Пример 1
def task_1(A):
    # TODO
    summ=0
    for ell in A:
        if ell > 0:
            summ+=int(ell)
    return summ


# Пример 2
def task_2(A):
    # TODO
    summ=0
    count=0
    for ell in A:
        summ+=int(ell)
        count+=1
    sr_arifm=summ/count
    return sr_arifm


# Пример 3
def task_3(A):
    # TODO
    return np.std(A)
