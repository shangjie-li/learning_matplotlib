# learning_matplotlib

Some code examples for learning matplotlib in Python

## 内容
 - 在`learning_matplotlib.py`中记录了一些利用matplotlib画图的代码示例，内容包括
    - 导入matplotlib模块
    - Figure对象
    - Axes实例：绘图类型、线条属性、图例、文本格式和注释、轴属性、高级布局
 - 参考
    - Numerical Python: Scientific Computing and Data Science Applications with NumPy, SciPy and matplotlib
    - Python科学计算和数据科学应用
    
## 附表
 - 表4-1 matplotlib绘图方法中线条的基本属性以及对应的关键字参数
   ```Shell
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
   ```
 - 表4-2 字体的部分属性以及对应的关键字参数
   ```Shell
   关键字参数         描述
   fontsize         文本字号，以磅为单位
   fontname         文本字体
   backgroundcolor  文本标签的背景颜色
   color            文本颜色
   alpha            文本颜色的透明度
   rotation         文本标签的旋转角度
   """
