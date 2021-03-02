# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#~ # ----------------------------------------------------------------------
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

#~ # ----------------------------------------------------------------------
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

#~ # ----------------------------------------------------------------------
#~ # 例3
#~ # fig是一个画布实例
#~ # axes是在画布中创建3行2列的坐标轴实例 <class 'numpy.ndarray'> (3, 2)
#~ fig, axes = plt.subplots(nrows=3, ncols=2)
#~ plt.show()

#~ # ----------------------------------------------------------------------
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

#~ plt.show()

# ----------------------------------------------------------------------
# 例5

