from py4cats import *
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import time

def mol_tau(self,gas, wav_min, wav_max, line_data, mls_data, profile_num, stop_requested):
	# 首先检查终止线程的标志
	if not stop_requested:
		mls = atmRead(mls_data)  # get atmosphere
		# atmRead所有返回的变量，均使用cgs单位制(z[cm],  p[dyn/cm**2],  T[K],  n[molec/cm**3])
		NA = 6.02e+23
		R = 8.31
		temp_mls = np.zeros((len(mls),len(mls[0])))
		name = ['z','pressure','T','air','H2O','CO2','O3','N2O','CO','CH4','O2','NO','SO2','NO2','NH3','HNO3','OH','HF','HCl','HBr','HI','ClO','OCS','H2CO','HOCl','N2','HCN','CH3Cl','H2O2','C2H2','C2H6','PH3','HO2']
		temp_mls[:,0] = mls['z'] /(1e+5)
		temp_mls[:,1] = mls['p'] /1000
		for i in range(len(name)-2):
			temp_mls[:,i+2] = mls[name[i+2]] # 分子数密度单位就用molec/m**3
		filename_mls = './dat/USS_' + profile_num + '.dat'
		np.savetxt(filename_mls, np.flipud(temp_mls), delimiter=' ', fmt='%10.5f', newline="\n")
																	
		# 设定大气中CO2的浓度
		# num = '409'

		# 设置CO2以及CH4的浓度
		# origin = int(num)
		# mls['CO2'] = mls['CO2'] * origin / 330
		# atmPlot(mls, what='CO2', vertical='km', vmr=True)

		dll = higstract(line_data, (wav_min,wav_max))  # Dictionary of Line Lists
		# 计算差分光学厚度
		od = lbl2od(mls, dll)

		# 更新进度条
		self.progressChanged.emit(40)
		# 定期检查终止线程的标志
		if stop_requested:
			self.progressChanged.emit(0)
			return

		length_od = []
		for i in range(len(od)):
			length_od.append(len(od[i].grid()))

		interp_lines = max(length_od)

		# 将计算结果保存在查找表中
		z = []
		# 高度从大到小排列
		for i in range(len(mls) - 1, -1, -1):
			# 将单位从 cm 转换为 km
			z.append(mls[i][0] / 1e+5)
		# 将一个 NumPy 数组 z 转换为整数类型, 然后把原来的一维数组重新排列为一个包含一行和 len(mls) 列的二维数组
		z = np.array(z, dtype= float).reshape((1, len(mls)))

		# 将生成的数据保存在文本文件中
		filename = 'mol_tau_file_' + gas + '.txt'
		np.savetxt(filename, z, delimiter=' ', fmt='%10.5f', newline="\n")
		# 以最大的grid()长度值为标准进行统一,也就是最细的波长网格(为什么od.grid()的长度随着高度的增加而增大)
		layer_od = od[0].regrid(interp_lines)
		wavelength = 1e+7 / layer_od.grid()
		# 构建需要写入的光学厚度数据矩阵
		temp = np.zeros((len(wavelength), len(mls)))
		# flipud将矩阵进行上下翻转，使wavelength从小到大排列
		temp[:, 0] = np.flipud(wavelength)
		for i in range(len(od) - 1, -1, -1):
			# od根据高度从大到小排列
			layer_od = od[i].regrid(interp_lines)
			# flipud将矩阵进行上下翻转，使layer_od与wavelength对应
			temp[:, len(mls)-1-i] = np.flipud(layer_od)

		with open(filename, 'a') as f:
			np.savetxt(f, temp, delimiter=' ', fmt='%10.20f', newline="\n")
		f.close()
