#fibonacci(n)
#-loop
#-recursive

#L_1=4,-3,5,-2,-1,2,6,-2

for i in range(i):
    for j in range(i,j):
        #print(i,j)
        for k in range(i,j):
            t=t+L2(k)
        if t>maxSum:
            maxSum=t

def my_sub_sum_recursive(List_1=[4,-3,5,-2,-1,2,6,-2]):

    if len(List_1)==1:
        return List_1[0]

    n=len(List_1)
    left_i=0
    left_j=n//2
    right_i=(n//2)
    right_j=n

    Left_sum=my_sub_sum_recursive(List_1[left_i:left_j]
    Right_sum=my_sub_sum_recursive(Liste_1[right_i:right_j])

    t,temp_left_sum=0,0
    for i in range(left_j,left_i,-1:
                t=t+List_1[i]
                if(t>temp_left_sum):
                    temp_left_sum=t

    t,temp_right_sum=0,0
          for i in range(right_j,right_i,-1:
                t=t+List_1[i]
                if(t>temp_right_sum):
                    temp_right_sum=t
                         
    center_sum=temp_left_sum+temp_right_sum



    def max_of_two(a,b):
            if a>b:
                return a
            else:
                return b

    def max_of_three(a,b,c)
            return max_of_two(a,max_of_two(b,c))

    return max_of_three(left_sum,right_sum,center_sum)


                    
        

    
                            

