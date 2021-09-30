import os
from openpyxl import load_workbook
from openpyxl.chart import LineChart, Reference

# 设置目标文件夹路径
path = './各部门利润表汇总/'

# 获取文件夹下的所有文件名
file_list = os.listdir(path)
# 遍历文件名列表，取得每一个文件名
for file_name in file_list:
    # 拼接文件路径
    file_path = path + file_name
    # 读取工作簿
    wb = load_workbook(file_path)
    # 读取工作簿中的活跃工作表
    ws = wb.active

    # 实例化 LineChart() 类，得到 LineChart 对象

    # 引用工作表的部分数据

    # 添加被引用的数据到 LineChart 对象

    # 添加 LineChart 对象到工作表中，指定折线图的位置

    # 引用工作表的表头数据

    # 设置类别轴的标签

    # 设置 x 轴的标题

    # 设置 y 轴的标题

    # 改变线条颜色

    # 保存文件
    wb.save(file_path)
# 打印"绘制Excel的图成功！"
print('绘制Excel的图成功！')