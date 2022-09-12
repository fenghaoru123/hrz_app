#coding=utf8
#
# def bubble(data, data_len):  # 自定义一个冒泡排序法函数
#     traversal_times = data_len - 1
#     for m in range(traversal_times, 0, -1):  # 遍历排序次数
#         # print (m)
#         for n in range(m):  # 遍历新数据QW
#             # print (n)
#             if data[n + 1] < data[n]:  # 如果数据小于原来的数据
#                 data[n], data[n + 1] = data[n + 1], data[n]  # 需要交换位置
#         print('第 %d 次排序之后的结果是' % (data_len - m), end='')  # 提示
#         for j in range(data_len):  # 遍历每次排序的结果
#             print('%3d' % data[j], end='')  # 输出结果
#         print()  # 输出空行
#
#
# num_list = [56, 20, 84, 66, 13]  # 创建数列并初始化20 56 66 13 84  =20 56 13 66 84 =20 13 56 66 84
# length = len(num_list)
# print("原始数据为：")  # 提示
# for i in range(length):  # 遍历原有数据
#     print('%3d' % num_list[i], end='')  # 输出结果
# print('\n---------------------------')  # 输出分界符
# bubble(num_list, length)  # 调用冒泡排序法函数
# print('---------------------------')  # 输出分界符
# print("排序之后的数据为：")  # 提示
# for i in range(length):  # 遍历排序好的新数列的数据
#     print('%3d' % num_list[i], end='')  # 输出结果
# print('')  # 输出空行
# #
# def maopao(date,lenth):
#     count=length - 1
#     for i in range(1,count,1):  #冒泡排序次数遍历
#         for j in range(i):
#             if date[j]<date[j+1]:
#                 date[j],date[j+1]=date[j+1],date[j]
#                 print ('第%d次的数据为：'%(i), end='')
#         for n in range(lenth):  # 遍历每次排序的结果
#             print('%3d' % date[n], end='')  # 输出结果
# maopao(num_list, length)


# num=1
# sum=0
# while num<101:
#     sum=sum+num
#     num+=1
# print (sum)
# num=0
# list=[]
# # while num<101:
# #     sum=sum+num
# #     num+=2
# while num<101:
#     if num%2==0:
#         list.append(num)
#     num+=2
#     print (sum(list))
#
# for i in range (1,10):
#     for j in range (1,10):
#         print (i,'*',j,'=',i*j, end='  ')
#         if i==j:
#             print('')
#             break
# for i in range (1,10):
#     for j in range (1,10):
#         if i==j:
#             print (i, '*', j, '=', i * j, end='  ')
#             break
#         else:
#             print (i, '*', j, '=', i * j, end='  ')


#
# for i in range(1, 10):
#     for j in range(i, 10):
#         print("%d*%d=%2d" % (i, j, i * j), end=" ")
#     print("")
str='duoceshi'











