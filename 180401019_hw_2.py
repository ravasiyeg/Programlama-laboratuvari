def get_months():
    my_list=[]
    f=open('input_hw_2.csv', 'r+')
    contents=f.readlines()
    for line in contents:
        month=line.rsplit("-",2)
        my_list.append(month[1])
    f.close()
    return my_list

lst_1=get_months()
my_list=lst_1

def my_frequency_with_dict(my_list):
    frequency_dict={} #dict()={}
    for item in my_list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
        return frequency_dict

my_frequency_with_dict(my_list)

def my_frequency_with_list_of_tuples(my_list):
    frequency_list=[]
    for i in range(len(my_list)):
        s=False
        for j in range(len(frequency_list)):
            if(lst_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([my_list[i],1])
    return frequency_list

result_1=my_frequency_with_dict(my_list)
result_2=my_frequency_with_list_of_tuples(my_list)
#print(result_2)


def my_bubble_sort(my_list):
    n=len(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list


my_bubble_sort(my_list)
my_list_2=my_frequency_with_list_of_tuples(my_list)
my_bubble_sort(my_list_2)


def get_number_of_people():
    my_list=[]
    n=len(my_list_2)
    for i in range(n):
        my_list.append(my_list_2[i][1])
    return my_list

def my_median(my_list):
    my_bubble_sort(my_list)
    n=len(my_list)
    if n%2==1:
        middle=int(n/2)+1
        median=my_list[middle-1]
        print("Medyan: ",median)
    else:
        middle_1=int(n/2)-1
        middle_2=middle_1+1  
        median=int(my_list[middle_1]+my_list[middle_2])/2
        print("Medyan: ",median)
    return median

def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean_= t/s
    print("Ortalama: ",mean_)
    return mean_



my_list_3=get_number_of_people()
median=my_median(my_list_3)
mean=my_mean(my_list_3)


output = ["Medyan : ",str(median),"Ortalama : ", str(mean)]

with open("180401019_hw_2_output.txt","w",encoding="utf-8") as write_file:
    for i in range(0,len(output),2):
        write_file.write(output[i] + " " + output[i+1] + "\n")
write_file.close()



