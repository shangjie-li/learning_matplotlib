# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

"""
表4-1 matplotlib绘图方法中线条的基本属性以及对应的关键字参数
------------------------------------------------------------------------------
关键字参数         描述             可选值
color            设置颜色          red、blue等，或形如#aabbcc的16进制颜色码
alpha            设置透明度        浮点数，介于0和1之间
linewidth        设置线宽          浮点数
linestyle        设置线型          -实线，--虚线，:点线，.-点画线
marker           设置标记的类型     +十字形，o圆形，*星形，s方形，.点形，1234为不同三角形
markersize       设置标记的大小     浮点数
markerfacecolor  设置标记的颜色     颜色值，与color的取值一样
markeredgewidth  设置标记边缘的线宽  浮点数
markeredgecolor  设置标记边缘的颜色  颜色值，与color的取值一样
------------------------------------------------------------------------------

表4-2 字体的部分属性以及对应的关键字参数
------------------------------------------------------------------------------
关键字参数         描述
fontsize         文本字号，以磅为单位
fontname         文本字体
backgroundcolor  文本标签的背景颜色
color            文本颜色
alpha            文本颜色的透明度
rotation         文本标签的旋转角度
------------------------------------------------------------------------------
"""

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例1
#~ x = np.linspace(-5, 2, 100)
#~ y1 = x ** 3 + 5 * x ** 2 + 10
#~ y2 = 3 * x ** 2 + 10 * x
#~ y3 = 6 * x + 10

#~ fig, ax = plt.subplots()
#~ ax.plot(x, y1, color='blue', label='y(x)')
#~ ax.plot(x, y2, color='red', label="y'(x)")
#~ ax.plot(x, y3, color='green', label='y"(x)')
#~ ax.set_xlabel('x')
#~ ax.set_ylabel('y')
#~ ax.legend()
#~ plt.show()

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例2
#~ # 画布宽8inch高2.5inch，f1=15*16+1
#~ fig = plt.figure(figsize=(8, 2.5), facecolor='#f1f1f1')

#~ # 坐标轴实例在画布实例中左下角坐标以及宽高所占的比例，e1=14*16+1
#~ left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
#~ ax = fig.add_axes((left, bottom, width, height), facecolor='#e1e1e1')

#~ x = np.linspace(-2, 2, 1000)
#~ y1 = np.cos(40 * x)
#~ y2 = np.exp(- x ** 2)

#~ ax.plot(x, y1 * y2)
#~ ax.plot(x, y2, 'g')
#~ ax.plot(x, - y2, 'g')
#~ ax.set_xlabel('x')
#~ ax.set_ylabel('y')

#~ # dpi单位为点/inch
#~ fig.savefig('graph.png', dpi=100, facecolor='#f1f1f1')

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例3
#~ # fig是一个画布实例
#~ # axes是在画布中创建3行2列的坐标轴实例 <class 'numpy.ndarray'> (3, 2)
#~ fig, axes = plt.subplots(nrows=3, ncols=2)
#~ plt.show()

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例4
#~ x = np.linspace(-5, 5, 5)
#~ y = np.ones_like(x)

#~ # 对坐标轴的设置
#~ def axes_settings(fig, ax, title, ymax):
    #~ # 不显示横轴、纵轴的刻度
    #~ ax.set_xticks([])
    #~ ax.set_yticks([])
    
    #~ # 设置横轴、纵轴的刻度范围
    #~ ax.set_xlim(-6, 6)
    #~ ax.set_ylim(0, ymax + 1)
    
    #~ # 设置标题
    #~ ax.set_title(title)
    
#~ # 在画布中创建1行4列的坐标轴实例
#~ fig, axes = plt.subplots(1, 4, figsize=(16, 3))

#~ # 在第一个坐标系中，线条宽度
#~ linewidths = [0.5, 1.0, 2.0, 4.0]
#~ for n, linewidth in enumerate(linewidths):
    #~ axes[0].plot(x, y + n, color='blue', linewidth=linewidth)
#~ axes_settings(fig, axes[0], 'linewidth', len(linewidths))

#~ # 在第二个坐标系中，线条类型
#~ linestyles = ['-', '--', '-.', ':']
#~ for n, linestyle in enumerate(linestyles):
    #~ axes[1].plot(x, y + n, color='blue', linewidth=2, linestyle=linestyle)
#~ axes_settings(fig, axes[1], 'linestyle', len(linestyles))

#~ # 在第三个坐标系中，标记类型
#~ markers = ['+', 'o', '*', 's', '.', '1', '2', '3', '4']
#~ for n, marker in enumerate(markers):
    #~ axes[2].plot(x, y + n, color='blue', linewidth=2, linestyle='-', marker=marker)
#~ axes_settings(fig, axes[2], 'markers', len(markers))

#~ # 在第四个坐标系中，标记大小和颜色
#~ markersizecolors = [(4, 'white'), (8, 'red'), (12, 'yellow'), (16, 'lightgreen')]
#~ for n, (markersize, markerfacecolor) in enumerate(markersizecolors):
    #~ axes[3].plot(x, y + n, color='blue', linewidth=1, linestyle='-', marker='o', markersize=markersize, markerfacecolor=markerfacecolor, markeredgewidth=2)
#~ axes_settings(fig, axes[3], 'marker size/color', len(markersizecolors))

#~ fig.savefig('marker.png', dpi=100)
#~ plt.show()

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例5
#~ x = np.linspace(-5, 2, 100)
#~ y1 = x ** 3 + 5 * x ** 2 + 10
#~ y2 = 3 * x ** 2 + 10 * x
#~ y3 = 6 * x + 10

#~ fig, ax = plt.subplots()
#~ ax.plot(x, y1, color='blue', label='y(x)')
#~ ax.plot(x, y2, color='red', label="y'(x)")
#~ ax.plot(x, y3, color='green', label='y"(x)')
#~ ax.set_xlabel('x')
#~ ax.set_ylabel('y')

#~ # 在Axes的外面显示图例
#~ # bbox_to_anchor指示顶点位置为横向1.02、纵向1
#~ # loc指示定位的顶点，1为图例右上角，2为图例左上角，3为图例左下角，4为图例右下角
#~ # ncol指示图例拆分的列数，不指明时默认为1列
#~ ax.legend(bbox_to_anchor=(1.02, 1), loc=2, ncol=2, borderaxespad=0.0)
#~ # 在Axes的右边设置图例的空间，坐标轴占0.7，图例占0.3
#~ fig.subplots_adjust(right=0.7)

#~ plt.show()

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例6
#~ fig, ax = plt.subplots(figsize=(12, 3))

#~ # 设置横轴、纵轴的刻度范围
#~ ax.set_xlim(-0.5, 3.5)
#~ ax.set_ylim(-0.05, 0.25)

#~ # 添加与横轴、纵轴平行的辅助线
#~ ax.axhline(0.0)
#~ ax.axvline(1.0)

#~ # 添加文本
#~ ax.text(0, 0.1, 'Text label', fontsize=14, fontname='serif')

#~ # 添加注释
#~ ax.plot(1, 0, 'o')
#~ ax.annotate('Annotation', fontsize=14, fontname='serif', xy=(1, 0), xycoords='data', xytext=(+ 20, + 50), textcoords='offset points',
 #~ arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.5'))
 
#~ # 添加方程
#~ ax.text(2, 0.1, r'Equation: $i\hbar\partial_t \Psi = \hat{H} \Psi$', fontsize=14, fontname='serif')

#~ plt.show()

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例7
#~ x = np.linspace(0, 50, 500)
#~ y = np.sin(x) * np.exp(- x / 10)

#~ # facecolor为画布实例设置颜色，subplot_kw中的facecolor为坐标轴实例设置颜色
#~ fig, ax = plt.subplots(figsize=(8, 2), facecolor='#f1f1f1', subplot_kw={'facecolor':'#ebf5ff'})

#~ ax.plot(x, y, linewidth=2)

#~ # labelpad为坐标轴与标签之间的距离，以磅为单位
#~ ax.set_xlabel('x', labelpad=5, fontsize=18, fontname='serif', color='blue')
#~ ax.set_ylabel('f(x)', labelpad=15, fontsize=18, fontname='serif', color='blue')

#~ # set_title中的loc参数可以设置标题对齐方式，左对齐left，居中center，右对齐right
#~ ax.set_title('axis labels and title example', loc='center', fontsize=16, fontname='serif', color='blue')

#~ plt.show()

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例8
#~ x = np.linspace(0, 30, 500)
#~ y = np.sin(x) * np.exp(- x / 10)

#~ fig, axes = plt.subplots(1, 3, figsize=(9, 3), subplot_kw={'facecolor': '#ebf5ff'})

#~ # 设置坐标轴的刻度范围
#~ axes[0].plot(x, y, linewidth=2)
#~ axes[0].set_xlim(-5, 35)
#~ axes[0].set_ylim(-1, 1)
#~ axes[0].set_title('set_xlim / set_ylim')

#~ # 设置坐标轴范围紧密匹配所绘数据
#~ axes[1].plot(x, y, linewidth=2)
#~ axes[1].axis('tight')
#~ axes[1].set_title('axis("tight")')

#~ # 设置横纵坐标轴比例相同
#~ axes[2].plot(x, y, linewidth=2)
#~ axes[2].axis('equal')
#~ axes[2].set_title('axis("equal")')

#~ plt.show()

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例9
#~ x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
#~ y = np.sin(x) * np.exp(- x ** 2 / 20)

#~ fig, axes = plt.subplots(1, 2, figsize=(8, 3))

#~ axes[0].plot(x, y, linewidth=2)
#~ axes[0].set_title('default ticks')

#~ # 设置坐标轴的刻度值
#~ axes[1].plot(x, y, linewidth=2)
#~ axes[1].set_title('set_xticks')
#~ axes[1].set_yticks([-1, 0, 1])
#~ axes[1].set_xticks([-5, 0, 5])

#~ plt.show()

#~ # --------------------------------------------------------------------------------------------------------------------------------------------
#~ # 例10
x = np.linspace(-10, 10, 500)
y = np.sin(x) / x

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, linewidth=2)

# 去除顶部和右侧的框线，spines是一个字典，其中的键包括right、left、top、bottom
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 将底部和左侧的框线移到x=0、y=0处
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 设置坐标轴的刻度值
ax.set_xticks([-10, -5, 5, 10])
ax.set_yticks([])

fig.savefig('axis.png', dpi=100)
plt.show()
