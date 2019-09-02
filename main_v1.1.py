#Version 1.1
import re
import codecs
import time
import easygui
import os
file = easygui.fileopenbox(default='*.txt')
(dir,tempfilename) = os.path.split(file)
print(dir)
f_in = codecs.open(file,'r','utf-8')
# f_in = open(file,'r',encoding='utf-8')
print(dir + '\\align_paper.txt')
f_out = open(dir + '\\align_paper.txt','w',encoding='utf-8')
content = f_in.read()
r_list = content.split("\r\n")
f_in.close()
list_paper = r_list
# print(list_paper)
r = len(r_list)
# index = 1
#将文本转化为列表
for index in range(r):
    #c = r_element.split('）') #没有括号不需要此语句
    # print(r_list[index])
    try:
        if '）' in r_list[index]:
            c = r_list[index].split('）', 1)
            c = c[1].split()
        else:    
            c = r_list[index].split('，')
    except:
        print('第%d行格式不正确' %(index+1))
        time.sleep(5)
        # exit()
    print(c)
    #c1.insert(0,c[0])
    # c = c1
    c.insert(0,str(index+1)+')'+c[0])
    del c[1]
    # print(r_element)

    list_paper[index] = c
    # index +=1
# print(list_paper)
# print(len(list_paper[0][4]))
list_count = [0,]*4
i = 1
for row in list_paper:
    for k in range(0,len(row)):
        # print(i)
        # print(len(row[k]))
        if k == 0:
            # 
            # pass
            print(i,':',len(row[0]))
        try:
            if(list_count[k]<len(row[k])):
                list_count[k] = len(row[k])
        except:    
            print('第%d行格式不正确' %i)
            time.sleep(5)
            # exit()
    i += 1        
print(list_count) 

sum_count = 0
for count in list_count:
    sum_count += count
if sum_count>45 :
    rest = sum_count - 46
print(rest)
list_count[1] -= rest
print(list_count[1])
# list_count[0] -= 1
# list_count[2] -= 1
tplt = "{0:{4}<%d}\t{1:{4}<%d}\t{4}{2:{4}<%d}\t{3:<%d}\n" % tuple(list_count)    
# print(tplt)
# index = 0
# for row in list_paper:
#     if len(row[1]) > list_count[1]:
#         f_out.write(tplt.format(row[0],row[1][:list_count[1]],row[2],row[3],chr(12288)))
#         # num = len(rwo[1]) - list_count[1]
#         # f_out.write(tplt.format(' ',row[1][-num:],' ',' ',chr(12288)))
#     else:
#         f_out.write(tplt.format((row[0],row[1],row[2],row[3],chr(12288)))
#         # tplt = "{0:<%d}\t{1:{5}<%d}\t{2:{5}<%d}\t{3:{5}<%d}\t{4:<%d}\n" % tuple(list_count)      
index = 0
for row in list_paper:
    if len(row[1]) > list_count[1]:
        # 
        print(index+1)
        print(row)
        f_out.write(tplt.format(row[0],row[1][:list_count[1]],row[2],row[3],chr(12288)))
        num_rest = len(row[1]) - list_count[1]
        f_out.write(tplt.format('  ',row[1][-num_rest:],'','',chr(12288)))
    else:
        f_out.write(tplt.format(row[0],row[1],row[2],row[3],chr(12288)))

    
    # tplt = "{0:<%d}\t{1:{5}<%d}\t{2:{5}<%d}\t{3:{5}<%d}\t{4:<%d}\n" % tuple(list_count)     
    index +=1    
f_out.close()

print('论文对齐完成！！！','请到源文件夹下查看align_paper.txt文件')
os.system('notepad %s' % dir + '\\align_paper.txt')
time.sleep(5)
exit()