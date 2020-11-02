# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:21:21 2020

@author: USER
"""
h = int(input("请输入起始高度：")) # 获取用户输入
c = 10
tour = [] # 总经过多少米赋值
height = [] # 第n次的高度

for i in range(1,c+1): # 利用for in对次数进行循环，次数的循环改变影响着总体的高度，在这里，对于总里程，我们将球落地时为一个循环
    if i == 1: # 当i为1的时候，将起始高度n添加到tour当中。
        tour.append(h)
    else: # 否则，将n循环后高度的一半加入到tour中，因为路程需要经历两次
        tour.append(2*h)
    h /= 2 # 第二次的高度为原始高度的一半
    height.append(h) # 将球每次的高度 加入到height列表当中
s = sum(tour) #对遍历所有i所得到路程结果进行求和
u = height[-1] #最后得到的一个高度

print("%d次经历的总路程为:%f"%(c,s)) # 输出对应的结果 %d,表示整数，%f表示浮点数。
print("第%d次的反弹高度为:%f"%(c,u))