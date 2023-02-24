


def task_1(list,a):
    stri=''
    for i in range(0,len(list)):
        if list[i]==a:
            stri=str(i)
            return stri

def task_2(x):
    for j in range(2,round(x**0.5)+1):
        if x%j==0:
            return False
    return True