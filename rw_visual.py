import matplotlib.pyplot as plt 

from random_walk import RandomWalk 
while True:
	# 创建一个Random实例，并将其包含的点都绘制出来
	rw = RandomWalk(50000)
	rw.fill_walk()

	# 设置绘图窗口的尺寸
	plt.figure(dpi=128,figsize=(10,6))
	# 绘制点并将图形显示出来
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolor='none', s=1)

	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("Make another walk? (y/n)")
	if keep_running == 'n':
		break


	