import math
def task_1(text):
    slovar={}
    counter=0
    str=" "
    for sym in text:
        if sym==".":
            for pr in str:
                if pr==" ":
                    counter+=1
            str=str.replace(' ','',1)
            slovar[str]=counter
            str=""
            counter=0
        else:
            str += sym


    return slovar

def task_2(x1,y1,x2,y2):
        x=abs(x1-x2)
        y=abs(y1-y2)
        res=math.sqrt(x*x + y*y)
        return res



