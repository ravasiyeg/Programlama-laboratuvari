def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        if b%2==0:
            return power(a*a,b//2)
        else:
            return power(a*a,b//2)*a


def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        t=1
        for i in range(b):
            t=t*a
            return t

#recursive

def power(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    if b>1:
        #return power(a,b-1)*a
               #power(a+a,b/2)




#sorting:
        bubblesort
        insertionsort
        selection
        heapsort
        quicksort


#örnek:
       # 4,-3,5,-2,-1,2,6,-2 toplamı fazla olan alt dizi?


def my_f_1():
    Liste_1=[4,-3,5,-2,-1,2,6,-2]
    max=0
    for i in range(8):
        for j in range(i+1,8):
            t=0
        #print(i,j)
    for k in range(i,j):
        t=t+Liste_1[k]
    if t>max:
        max=t
         i_1,i_2=i_3
        return max,i_1,i_2






    
