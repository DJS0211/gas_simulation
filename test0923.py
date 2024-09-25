import py4cats
import numpy as np
import itertools
from scipy.io import savemat
from netCDF4 import Dataset
import dill as pickle
import copy
from py4cats.art.xSection import xsArray

# 示例使用
T_list = np.arange(219, 289, 2)
P_list = np.arange(1*1000, 71*1000, 2*1000)

# 从 HITRAN 数据中获取 line data
dictLineLists = py4cats.higstract('./HITRAN_data/HITRAN_CO2_1.par', (3333, 3337))

# 使用 itertools.product 生成所有温度和压强的组合
result = list(itertools.product(T_list, P_list))

# 将结果转换为 numpy 数组进行输出
result_array = np.array(result)

# 提取 result_array 的第一列和第二列
T_list_extracted = result_array[:, 0]
P_list_extracted = result_array[:, 1]
# 大气数据
mls = py4cats.atmRead('./USS/USS_16 copy.xy')

# 调用 py4cats.lbl2xs 计算吸收截面
xs_Array = py4cats.lbl2xs(dictLineLists['CO2'], mls['p'], mls['T'], sampling=1.0, nGrids=1)

ac_Array = py4cats.xs2ac(mls,xs_Array)

def manual_deepcopy(xs):
    new_xs = xsArray(xs.view(np.ndarray).copy(), xLimits=copy.deepcopy(xs.x), p=copy.deepcopy(xs.p), t=copy.deepcopy(xs.t), molec=copy.deepcopy(xs.molec), lineShape=copy.deepcopy(xs.lineShape))
    return new_xs
# 创建一个存储匹配结果的列表
matched_xsArray = []
# 遍历 mls 中的每一组压强和温度组合，找到对应的 xsArray
for i in range(len(mls['p'])):
    p_mls = mls['p'][i]  # 当前大气压强
    t_mls = mls['T'][i]  # 当前大气温度

    # 分别找到最接近的 p 和 t

    closest_p = min(xs_Array, key=lambda xs: abs(xs.p - p_mls))
    closest_t = min(xs_Array, key=lambda xs: abs(xs.t - t_mls))
    # 遍历 xs_Array，寻找同时满足最接近的 p 和 t 的元素
    for xs in xs_Array:
        if xs.p == closest_p.p and xs.t == closest_t.t:
            # xs_temp = xs
            # xs_temp = copy.deepcopy(xs)  # 创建xs的深拷贝
            xs_temp = manual_deepcopy(xs)
            xs_temp.p = p_mls
            xs_temp.t = t_mls
            matched_xsArray.append(xs_temp)
            break

od = py4cats.xs2dod(mls,matched_xsArray)