import pickle
import py4cats
import dill as pickle
import numpy as np
import copy
from py4cats.art.xSection import xsArray
from py4cats.var.pairTypes import Interval

with open('xs_Array.pkl', 'rb') as f:
    xs_Array = pickle.load(f)
# print(xs_Array[0].molec)  # 检查具体的 molec 属性值
# 大气数据
mls = py4cats.atmRead('./USS/USS_16 copy.xy')
# 创建一个存储匹配结果的列表
matched_xsArray = []

def manual_deepcopy(xs):
    new_xs = xsArray(xs.view(np.ndarray).copy(), xLimits=copy.deepcopy(xs.x), p=copy.deepcopy(xs.p), t=copy.deepcopy(xs.t), molec=copy.deepcopy(xs.molec), lineShape=copy.deepcopy(xs.lineShape))
    return new_xs

# 目标波数范围
x_min, x_max = 3357, 3365

# 根据波数范围截取吸收截面数据
truncated_xsArray = []  # 用于存储截取后的数组
# 遍历 xs_Array 中的每个元素
for xs in xs_Array:
    # truncated_array = manual_deepcopy(xs)
    # # 找到满足波数范围 (x_min, x_max) 的索引
    # indices = np.where((xs.grid() >= x_min) & (xs.grid() <= x_max))[0].tolist()
    # # truncated_array. = xs[indices]  # 截取对应的吸收截面值
    # truncated_array.base = xs.view(np.ndarray)[indices]
    # truncated_array.x.lower = xs.x[indices]  # 截取对应的
    # truncated_array.p = xs.p[indices]  # 截取对应的
    # truncated_array.t = xs.t[indices]  # 截取对应的
    # truncated_xsArray.append(truncated_array)  # 将截取后的结果添加到列表中

    # 尝试直接根据截取后的值新建一个truncated_array，而不是先复制后截取
    indices = np.where((xs.grid() >= x_min) & (xs.grid() <= x_max))[0].tolist()
    xs_wavenumber_range = xs.grid()[indices]
    xLimits = Interval(float(xs_wavenumber_range[0]),float(xs_wavenumber_range[-1]))
    truncated_array = xsArray(xs.view(np.ndarray)[indices],xLimits,xs.p,xs.t,xs.molec,xs.lineShape)
    truncated_xsArray.append(truncated_array)  # 将新建的xsArray添加到列表中

# 遍历 mls 中的每一组压强和温度组合，找到对应的 xsArray
for i in range(len(mls['p'])):
    p_mls = mls['p'][i]  # 当前大气压强
    t_mls = mls['T'][i]  # 当前大气温度

    # 分别找到最接近的 p 和 t
    closest_p = min(truncated_xsArray, key=lambda xs: abs(xs.p - p_mls))
    closest_t = min(truncated_xsArray, key=lambda xs: abs(xs.t - t_mls))
    # print(closest_p,closest_t)
    # 遍历 truncated_xsArray，寻找同时满足最接近的 p 和 t 的元素
    for xs in truncated_xsArray:
        if xs.p == closest_p.p and xs.t == closest_t.t:
            # xs_temp = xs
            # xs_temp = copy.deepcopy(xs)  # 创建xs的深拷贝
            xs_temp = manual_deepcopy(xs)
            xs_temp.p = p_mls
            xs_temp.t = t_mls
            # print(f"Comparing: xs.p = {xs.p}, closest_p.p = {closest_p.p}")
            # print(f"Comparing: xs.t = {xs.t}, closest_t.t = {closest_t.t}")
            matched_xsArray.append(xs_temp)
            break

dod = py4cats.xs2dod(mls,matched_xsArray)
od = py4cats.dod2tod(dod)