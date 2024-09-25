import py4cats
import time

start_time = time.time()

line_data = './HITRAN_data/HITRAN_CO2_all.par'
mls_data = './USS/USS_16.xy' #廓线数据

dictLineLists = py4cats.higstract(line_data,(6155,6365))
mls = py4cats.atmRead(mls_data,extract='CO2')
dodList = py4cats.lbl2od(mls,dictLineLists)
todList = py4cats.dod2tod(dodList)

column_kurudz_wav = []
# 读取太阳光谱kurudz_0.01nm.txt里的波长值
with open('kurudz_0.01nm.txt','r') as f:
    lines = f.readlines()
f.close()
for line in lines :
    parts = line.split()
    if not parts[0].startswith('#'):
        column_kurudz_wav.append(float(parts[0]))

wavelength_min_threshold = 1 / (todList.grid()[-1] * 10**(-7))
wavelength_min_input = min((wav for wav in column_kurudz_wav if wav > wavelength_min_threshold),
                           key=lambda x: abs(x - wavelength_min_threshold))
# 找到与wavelength_max最接近的小于给定值的波长
wavelength_max_threshold = 1 / (todList.grid()[0] * 10**(-7))
wavelength_max_input = min((wav for wav in column_kurudz_wav if wav < wavelength_max_threshold),
                           key=lambda x: abs(x - wavelength_max_threshold))

# # 找到第一个大于wavelength_min的波长值(这一行很耗时间，所以设置一个检查点)
# wavelength_min_input = min([wav for wav in column_kurudz_wav if wav > 1/(todList.grid()[-1]*10**(-7))])
# # 找到第一个小于wavelength_max的波长值(这一行很耗时间，所以设置一个检查点)
# wavelength_max_input = max([wav for wav in column_kurudz_wav if wav < 1/(todList.grid()[0]*10**(-7))])

end_time = time.time()
elapsed_time = end_time - start_time

print('完成计算')
print(f"代码运行时间: {elapsed_time:.6f} 秒")
