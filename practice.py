# 1、知枫为了解决口味选择困难，把楼下的餐厅都整理起来了。但是很可惜，他最爱的【兰州拉面】转让给了【长沙臭豆腐】，所以需要【更改】餐厅列表的值并打印出来。
# '肯德基'、'兰州拉面'、'椰子鸡'、'沙县小吃'、'必胜客'、'海底捞'

lunch = ['肯德基','兰州拉面','椰子鸡','沙县小吃','必胜客','海底捞']
lunch[1] = '長沙臭豆腐'
print(lunch)



# 2、知枫早上上班的时候，大川让他去市场看看有没有卖包子的，有的话就帮忙买10个包子当大家的早餐，如果有看到卖西瓜的，就买一个。回公司之后，知枫用代码复现了早上这个小插曲。
market = ['包子','西瓜']

if '包子' in market:
    if '西瓜' in market:
        print('买了一个包子')
    else:
        print("买了10个包子")
else:
    print('没有卖包子的')



# 3、闪光小学班上共有10个学生，本次期末考试考了语文、数学、英语共3个科目，成绩储存在一个大列表scores里，大列表中有3个小列表chinese、math、english储存了各科成绩。请打印出60分以上的成绩。
# 成绩已经存在列表里了：
# scores列表里嵌套了三个科目的列表
chinese = [55, 60, 95, 90, 88, 87, 61, 59, 78, 90]
math = [66, 77, 90, 99, 58, 69, 77, 88, 82, 95]
english = [100, 98, 66, 43, 66, 47, 91, 67, 89, 59]
scores = [chinese, math, english]

for subject in scores:
    
    pass_score = []
    for s in subject:
        if s > 60:
            pass_score.append(s)
    if subject == chinese:
        print('语文考试及格的成绩有{}'.format(pass_score))
    elif subject == math:
        print('数学考试及格的成绩有{}'.format(pass_score))
    elif subject == english:
        print('英语考试及格的成绩有{}'.format(pass_score))



# 4、知枫想设计出一个猜数字的程序，要求是使用随机函数随机生成一个1到10以内的数字，然后再来猜测它，如果猜的结果比生成的数字大，系统提示“猜大了！”，如果猜的结果比生成的数字小，系统提示“猜小了！”，否则提示“猜对了”，最后猜对的时候系统反馈猜测的总次数。
# 提示：随机函数需要使用random模块，使用方法如下
# 生成1到10之间的随机数
import random
target = random.randint(1,10)
n = 1
print(target)
guess_num = int(input('范围1~10的整数，猜猜看这个数是什么： '))
while guess_num != target:
    
    if guess_num > target:
        guess_num = int(input('猜大啦！再猜一次： '))
        n += 1
    elif guess_num < target:
        guess_num = int(input('猜小啦！再猜一次： '))
        n += 1
print('猜對啦！一共猜了' + str(n) + '次')
    



# 5、闪光图书馆新进了一批图书，想分一部分比较多的书籍给闪光小学，请完成以下两个任务：
# 1.筛选出图书本数大于5的书籍，并把书名打印出来。
# 2.将数量大于5的书籍的数量改为“分配”；数量小于等于5的书籍的数量改为“自留”
# 书籍已经存在字典中了：
# 所有的书和数量都以字典的形式储存
books_dic = {'82年生的金智英': 3, '了不起的盖茨比': 6,'乌合之众': 5, '活着': 8, '小王子': 6, '设计的意义': 2}
print('数量大于5本的书籍有：')
for name in books_dic:
    if books_dic[name] > 5:
        print(name)
        books_dic[name] = '分配'
    else :
        books_dic[name] = '自留'
print(books_dic)



# 6、知枫要尝试编写一个程序，使其可以在终端打印出一个九九乘法表
# 提示：从上往下看，每一行最大的列值就是行值，如2X2=4与3x3=9，第2行只有2列，第3行只有3列。单独一行来看，列数是逐渐增加的，直到跟行数一致就换列，那么我们可以使用for循环结合range()来实行逐渐增加列数的操作。从整体来看，行数也是逐渐增加的，直到9为止，那么我们同样也开始用for循环来实现。

# 也就是说，我们可以使用一个for循环嵌套for循环来实现功能。外层和内层的循环分别用来管理行的输出和列的输出。
# 但是为了更美观，我们还需要控制式子的间隔以及上下的换行、输出。
# print('字符串',end='\t')可以在字符串后面保持间隔的一致（原意是添加一个制表符，即是tab）。
# print()函数会默认换行，可以单独使用，用于换行，让结果更美观。


for y in range(1,10):
    for x in range(1,y + 1):
        print(str(x) + 'X' + str(y) + '=' + str(x*y),end='\t')
    print()




# 7、计算出闪光小学一年1班各同学的总分，和班级的各科平均分。
# 各同学成绩存在字典中：
# 分数以字典嵌套列表存储，列表中依次为语文、数学、英语的成绩
scores = {'小李': [95, 98, 90], '小花': [96, 90, 94],
          '小华': [85, 80, 90], '小胖': [87, 94, 89],
          '小红': [79, 85, 90]
}


for name in scores:
    score = 0
    for subject in scores[name]:
        score += subject
    scores[name].append(score)
    print('{}的总分是{}'.format(name,score))

ch_sum = 0
ma_sum = 0
en_sum = 0
n = 0
for i in scores:
    ch_sum += scores[i][0]
    ma_sum += scores[i][1]
    en_sum += scores[i][2]
    n += 1
ch_avg = ch_sum/n
ma_avg = ma_sum/n
en_avg = en_sum/n
print('''
语文的平均分是{}
数学的平均分是{}
英语的平均分是{}'''.format(ch_avg,ma_avg,en_avg))


# 8、知枫想给家里的门设置一个密码锁，输入198764就可以成功解锁，一共只有5次
# 解锁机会，每输错一次就会提示你已经只剩下几次机会了，直到5次机会全部用完。
# 要求：用while和for循环两个知识点分别为小红家的密码锁设置一个程序。

#while迴圏 
answer = 198764
n = 5
while n > 0:
    password = int(input('请输入6位数密码，你剩{}次机会: '.format(n)))
    if password == answer:
        print('门开啦！')
        break
    else :
        print('密码不正确！')
        n -= 1
    if n <= 0:
        print('你没有机会了！')

# for迴圏
answer = 198764
for n in range(1,6):
    password = int(input('请输入6位数密码，你剩{}次机会: '.format(6-n)))
    if password == answer:
        print('门开啦！')
        break
    else :
        print('密码不正确！')
        if n == 5:
            print('你没有机会了！')



# 9、不知道你有没有过用镜子看书的体验，是不是发现字的顺序和我们正常看书的顺序是不同的，
# 那我们是不是可以通过代码实现镜子里面文字顺序的反转，变成正常看书的顺序呢？请思考下，如何实现吧。
# 提示：对于字符串的反转，可以使用len()函数来求得字符串的长度，再根据字符串长度，
# 采用循环去倒序遍历；也可以使用反向切片来实现

answer = '業企國跨的名著家一是，技生芯唐'
n = -1
new_answer = ''
for i in answer:
    new_answer = i + new_answer
print(new_answer)
