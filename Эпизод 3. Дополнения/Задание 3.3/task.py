def task_1(list):
    slovar={}
    for sym in list:
        if sym != ' ' and sym != '1':
            if sym in slovar:
                slovar[sym] += 1
            else:
                slovar[sym] = 1
    for y in slovar.items():
        if y[1]==max(slovar.values()):
            return y[0]

def task_2(x,y):
    x_chod=0
    y_chod=0
    ans=''
    for i in range(0,7):
        x_chod=x[i]
        y_chod=y[i]
        while x_chod<8 and y_chod<8:
            x_chod+=1
            y_chod+=1
            for j in range(i+1,8):
                if x[j]==x_chod and y[j]==y_chod:
                    ans='YES'
                    return ans
        x_chod = x[i]
        y_chod = y[i]
        while x_chod > 2 and y_chod > 2:
            x_chod -= 1
            y_chod -= 1
            for j in range(i+1, 8):
                if x[j] == x_chod and y[j] == y_chod:
                    ans = 'YES'
                    return ans
        x_chod = x[i]
        y_chod = y[i]
        while x_chod < 8 and y_chod > 2:
            x_chod += 1
            y_chod -= 1
            for j in range(i+1, 8):
                if x[j] == x_chod and y[j] == y_chod:
                    ans = 'YES'
                    return ans
        x_chod = x[i]
        y_chod = y[i]
        while x_chod > 2 and y_chod < 8:
            x_chod -= 1
            y_chod += 1
            for j in range(i+1, 8):
                if x[j] == x_chod and y[j] == y_chod:
                    ans = 'YES'
                    return ans


    ans='NO'
    return ans

def task_3(x,y,xc,yc,r):
    if (x-xc)^2+(y-yc)^2<=r^2:
        return False
    else:
        return True

def task_4(list):
    ans=0
    for i in range(1,len(list)-2):
        sosed_min=list[i-1]
        sosed_max=list[i+1]
        if list[i]> sosed_max and list[i]>sosed_min:
            ans+=1
    return ans

def task_5(key):
    list=[]
    alfavit = 'abcdefghijklmnopqrstuvwxyz'
    new_line=''
    with open("file.txt",'r') as f:
        for line in f:
            for sym in line:
                new_mesto=alfavit.find(sym)+key
                if new_mesto>len(alfavit):
                    new_mesto%=len(alfavit)
                if sym in alfavit:
                    new_line+=alfavit[new_mesto]
                else:
                    if sym==' ':
                        new_line+=alfavit[key-1]
            list.append(new_line)
            new_line=''


    return list
