#Bubble sort
def my_bubble(List_1):
    for i in range(len(List_1),0,-1):
        for j in range(i):
            if List_1[j]>List_1[j+1]:
                t=List_1[j+1]
                List_1[j+1]=List_1[j]
                List_1[j]=t
        return List_1


#bubble sortla dizi boyu en uzun kaç karşilastirma yapilabilir
#Comparison-> n.(n+1)/2
#swap

for i in range(n):
    for j in range(i,n):
        print(i,j)


def my_f_2(List_1=[4,-3,5,-2,-1,2,6,-2]):
    n=len(List_1)
    maxSum=0
    for i in range(n):
        t=0
        for j in range(i,n):
            t=t+List_1[j]
            if t>maxSum:
                maxSum=t
        return maxSum
    
#Recursive
    def my_f_3(List_1=[4,-3,5,-2,-1,2,6,-2]):
        n=len(List_1)
        if(n==1):
            return List_1[0]
        left_i=0
        left_j=n//2
        right_i=n//2
        right_j=n
        left_sum=my_f_3(List_1[left_i,left_j])
        right_sum=my_f_3(List_1[right_i,right_j]
        
