import py4cats
import numpy as np
import itertools
from scipy.io import savemat
from netCDF4 import Dataset
import dill as pickle

# 计算吸收截面（xs）
def compute_absorption(dictLineLists, T_list, P_list):
    # 使用 itertools.product 生成所有温度和压强的组合
    result = list(itertools.product(T_list, P_list))

    # 将结果转换为 numpy 数组进行输出
    result_array = np.array(result)

    # 提取 result_array 的第一列和第二列
    T_list_extracted = result_array[:, 0]
    P_list_extracted = result_array[:, 1]

    # 调用 py4cats.lbl2xs 计算吸收截面
    xs_Array = py4cats.lbl2xs(dictLineLists['CO2'], P_list_extracted, T_list_extracted, sampling=0.01, nGrids=1)
    # 假设 xsArray 是你要保存的变量
    with open('xs_Array.pkl', 'wb') as f:
        pickle.dump(xs_Array, f)
    return xs_Array

# # 示例使用
# T_list = np.arange(217, 291, 2)
# P_list = np.arange(0.05*1000, 1010*1000, 0.5*1000)

T_list = np.arange(217, 291, 2)   # 步长为 2
# 生成不同步长的序列
P_part1 = np.arange(0.05*1000, 10*1000, 0.5*1000)   # 步长为 0.5
P_part2 = np.arange(10*1000, 20*1000, 2*1000)   # 步长为 2
P_part3 = np.arange(20*1000, 100*1000, 5*1000)  # 步长为 5
P_part4 = np.arange(100*1000, 1020*1000, 10*1000)  # 步长为 10
# 使用 concatenate 将它们拼接成一个序列
P_list = np.concatenate([P_part1, P_part2, P_part3, P_part4])

# 从 HITRAN 数据中获取 line data
dictLineLists = py4cats.higstract('./HITRAN_data/HITRAN_CO2_1.par', (3355, 3370))

# 计算吸收截面
xs_Array = compute_absorption(dictLineLists, T_list, P_list)