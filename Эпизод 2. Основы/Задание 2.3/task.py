# todo: replace this with an actual task
def task_1(str):
    # TODO
    counter=0
    for sim in str:
        if sim==' ':
            counter=0
        else:
            counter+=1
    return counter


def task_2(str):
    # TODO
    st_1=''
    st_2=''
    st=''
    checker=True
    for sim in str:
        if checker==True:
            st_1+=sim
            if sim==' ':
                checker=False
        else:
            st_2+=sim
            if sim == ' ':
                st+=st_2+st_1
                st_1=''
                st_2= ''
                checker=True

    if st_2!=' ':
        st+=st_2
    if st_1!=' ':
        st+=st_1
    return st


def task_3(str):
    # TODO
    counter = 0
    ell=' '
    for sim in str:
        if ell==sim:
            counter+=1
        if sim!=' ':
            ell=sim



    return counter
