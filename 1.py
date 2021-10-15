from openpyxl import load_workbook
from openpyxl import Workbook
import os
import cn2an

# 获取文件夹中的文件名称
path = '高效办公实战训练营\\1\第1关\static\销售数据\\'
files = os.listdir(path)
# 设定存储总表数据和表头数据的空列表
total_row = []
head_row = []
# 遍历销售数据资料夹的所有文件名
for file in files:
    file_path = path + file
    # 以文件名打开工作簿、工作表
    wb = load_workbook(file_path)
    ws = wb.active
    # 读取工作表第二行之后的内容
    for row in ws.iter_rows(min_row=2,values_only=True):
        # 将元组转换为列表以便添加、修改元素
        row = list(row)
        # 获取文件名称(销售组别)以便添加进内容中
        group = file.split('.')
        # 计算总销售数量
        total_num = sum(row[2:])
        # 添加组别至列表第二个位置
        row.insert(1,group[0])
        # 添加总销售数量至列表末尾
        row.append(total_num)
        # 将列表嵌套至总列表中做循环
        total_row.append(row)
# 以降序的形式对整个列表重新排序，取值为每个列表的最后一个元素        
total_row = sorted(total_row,key=lambda a:a[-1],reverse=True)
# 对列表进行索引并添加到最后一位
for index,row in enumerate(total_row,start=1):
    row.append(index)
# 遍历任意销售表的第一行存成表头
for item in ws[1]:
    head_row.append(item.value)
# 添加表头数据
head_row.insert(1,'销售小组')
head_row.append('总计/瓶')
head_row.append('销售排名')

# 新建《销售总表》的工作表
wb_new = Workbook()
ws_new = wb_new.active
# 写入表头
ws_new.append(head_row)
# 写入全部值
for row in total_row:
    ws_new.append(row)
# 储存《销售总表》到对应路径
wb_new.save('高效办公实战训练营\\销售总表.xlsx')

# 设定《等级销售表》文件夹路径
path2 = '高效办公实战训练营\等级销售表\\'
# 判断路径是否存在，不存在的话新建文件夹
if not os.path.exists(path2):
    os.mkdir(path2)
# 设定每个等级的人数以及总共有几个等级
cut = 120
level = 4
# 从等级一开始新建工作表，循环
for num in range(level):
    wb_level = Workbook()
    ws_level = wb_level.active
    # 写入表头
    ws_level.append(head_row)
    # 反复切片120个值存进新的工作表中
    for row in total_row[num*cut:(num+1)*cut]:
        ws_level.append(row)
    # 储存工作簿，对文件名称进行数字-中文数字的转换
    wb_level.save(path2 + '等级{}销售表.xlsx'.format(cn2an.an2cn(num+1)))

