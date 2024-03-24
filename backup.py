from PySide6.QtCharts import QChartView
    # # 绘制透过率图
    # tranList = np.exp(-2*todList)
    # fig=plt.figure(figsize=(1050/100, 750/100),dpi=100,facecolor='none')
    # ax = fig.add_subplot(111)  # 添加子图
    # # 以防透过率对应的横坐标出错，这里使用todList的横坐标数据
    # ax.plot(todList.grid(),tranList.base,linewidth=3, color = 'yellow', alpha=1.0)
    # # 添加横纵坐标标注
    # ax.set_xlabel('Wavenumber/$cm^{-1}$',fontsize = 25)
    # ax.set_ylabel('transmittance',fontsize = 25)
    # # 设置横坐标只出现三个刻度
    # xticks = [wav_min,(wav_min+wav_max)/2,wav_max]
    # ax.set_xticks(xticks)
    # # 设置坐标轴的颜色为白色
    # ax.spines['bottom'].set_color('white')
    # ax.spines['top'].set_color('white')
    # ax.spines['left'].set_color('white')
    # ax.spines['right'].set_color('white')
    # # 设置坐标轴标签的颜色为白色
    # ax.xaxis.label.set_color('white')
    # ax.yaxis.label.set_color('white')
    # # 设置坐标轴刻度的颜色为白色，字体大小为25
    # ax.tick_params(axis='both', colors='white',labelsize = 25)
    # # 启用网格线
    # ax.grid(True)
    # # 保存图片
    # plt.savefig('plot_tran.png', transparent=True)
    # MainWindow.label_tran.setStyleSheet("border-image: url(./plot_tran.png);")
import matplotlib.pyplot as plt
import py4cats
mls = py4cats.atmRead('D:/project_gas_simulation/data/atmos/15/mls.xy')
py4cats.atmPlot(mls,'T','z')
plt.savefig('./picture/T.png')
py4cats.atmPlot(mls,'p','z')
plt.savefig('./picture/p.png')
py4cats.atmPlot(mls,'H2O','z')
plt.savefig('./picture/H2O.png')


    # # 绘制大气模式-温度图
    # fig=plt.figure(figsize=(700/100, 600/100),dpi=100,facecolor='none')
    # ax = fig.add_subplot(111)  # 添加子图
    # ax.plot(mls['T'],py4cats.unitConversion(mls['z'], 'length', new='km'),linewidth=3, color = 'yellow', alpha=1.0)
    # # 添加横纵坐标标注
    # ax.set_xlabel('Temperature / K', fontsize = 20)
    # ax.set_ylabel('Altitude / km', labelpad=1 , fontsize = 20)
    # # 设置坐标轴的颜色为白色
    # ax.spines['bottom'].set_color('white')
    # ax.spines['top'].set_color('white')
    # ax.spines['left'].set_color('white')
    # ax.spines['right'].set_color('white')
    # # 设置坐标轴标签的颜色为白色
    # ax.xaxis.label.set_color('white')
    # ax.yaxis.label.set_color('white')
    # # 设置坐标轴刻度的颜色为白色
    # ax.tick_params(axis='both', colors='white',labelsize = 20)
    # # 启用网格线
    # ax.grid(True)
    # # 保存图片
    # plt.savefig('./mode_picture/T.png', transparent=True)
    # MainWindow.label_tem.setStyleSheet("border-image: url(./mode_picture/T.png);")

    # # 绘制大气模式-湿度图
    # H2O = [7.74e+03,6.07e+03,4.63e+03,3.18e+03,2.16e+03,925,367,70,5,3.9,4.43,4.72,5.03,5.22,4.75,3.5]
    # fig=plt.figure(figsize=(700/100, 600/100),dpi=100,facecolor='none')
    # ax = fig.add_subplot(111)  # 添加子图
    # ax.plot(H2O,py4cats.unitConversion(mls['z'], 'length', new='km'),linewidth=3, color = 'yellow', alpha=1.0)
    # # 添加横纵坐标标注
    # ax.set_xlabel('ppm',labelpad=1 , fontsize = 20)
    # ax.set_ylabel('Altitude / km', labelpad=1 , fontsize = 20)
    # # 设置坐标轴的颜色为白色
    # ax.spines['bottom'].set_color('white')
    # ax.spines['top'].set_color('white')
    # ax.spines['left'].set_color('white')
    # ax.spines['right'].set_color('white')
    # # 设置坐标轴标签的颜色为白色
    # ax.xaxis.label.set_color('white')
    # ax.yaxis.label.set_color('white')
    # # 设置坐标轴刻度的颜色为白色
    # ax.tick_params(axis='both', colors='white',labelsize = 20)
    # # 启用网格线
    # ax.grid(True)
    # # 保存图片
    # plt.savefig('./mode_picture/H2O.png', transparent=True)
    # MainWindow.label_H2O.setStyleSheet("border-image: url(./mode_picture/H2O.png);")
    
    # # 绘制大气模式-压强图
    # fig=plt.figure(figsize=(700/100, 600/100),dpi=100,facecolor='none')
    # ax = fig.add_subplot(111)  # 添加子图
    # ax.plot(mls['p'],py4cats.unitConversion(mls['z'], 'length', new='km'),linewidth=3, color = 'yellow', alpha=1.0)
    # # 添加横纵坐标标注
    # ax.set_xlabel(r'Pressure $p \rm\,[g/cm/s^2]$',labelpad=1 , fontsize = 20)
    # ax.set_ylabel('Altitude / km', labelpad=1 , fontsize = 20)
    # # 设置坐标轴的颜色为白色
    # ax.spines['bottom'].set_color('white')
    # ax.spines['top'].set_color('white')
    # ax.spines['left'].set_color('white')
    # ax.spines['right'].set_color('white')
    # # 设置坐标轴标签的颜色为白色
    # ax.xaxis.label.set_color('white')
    # ax.yaxis.label.set_color('white')
    # # 设置坐标轴刻度的颜色为白色
    # ax.tick_params(axis='both', colors='white',labelsize = 20)
    # # 启用网格线
    # ax.grid(True)
    # # 保存图片
    # plt.savefig('./mode_picture/p.png', transparent=True)
    # MainWindow.label_pre.setStyleSheet("border-image: url(./mode_picture/p.png);")