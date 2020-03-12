list_1=get_words()
get_hist(List_1)

import os
my_List=os.Listdir()
for item in my_List:
    if os.path.isdir(item):
        print(item)


for item in my_List:
   if os.path.isfile(item):

dir_s=[dir for dir in my_List if os.path.isdir(dir)]
file_s=[file for file in my_List if os.payh.isfile(file)]

dir_s,file_s

def get_hist(path_1):
    file_s=[file for file in my_List if os.path.isfile(file)]
    return file_s

List_1=get_words()
get_hist(List_1)


def get_files(path_1):
    file_s=[file for file in my_List if os.path.isfile(file)]
    return file_S

List_1=get_words()
get_hist(List_1)

my_List=os.Listdir()

def get_words(my_file=u"C:\\Users\\COMU\\Documents\\data.txt"):
    my_List[ ]
    f=open(my_file,"r+")
    contents=f.readlines()
    for line in contents:
        #print(line)
        words=line.split(" ")
        for word in words:
            #print(word)
            my_List.append(word)
    #print(contents)
    f.close()
    return my_List

def get_hist(my_List):
    my_hist={}
    for w in my_List:
        if w in my_hist.keys():
            my_hist[w]=my_hist[w]+1
        else:
            my_hist[w]=1
    return my_hist


